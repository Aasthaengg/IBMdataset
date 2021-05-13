# https://atcoder.jp/contests/abc098/tasks/arc098_b

N = int(input())
A = list(map(int, input().split()))


# しゃくとり法
res = 0
right = 0
sum_a = 0
for left in range(N):
    while right < N and (sum_a ^ A[right]) == (sum_a + A[right]):
        sum_a += A[right]
        right += 1
    res += right - left
    
    # update
    if left == right:
        right += 1
    else:
        sum_a ^= A[left]

print(res)