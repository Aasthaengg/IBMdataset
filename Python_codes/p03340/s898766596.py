N = int(input())
A = list(map(int, input().split()))

ans = 0
tmp = A[0]
end = 0

# ^ = XOR演算子
for start in range(N):

    while end < N - 1 and (tmp ^ A[end + 1] == tmp + A[end + 1]):
        end += 1
        tmp += A[end]

    ans += (end - start + 1)
    tmp -= A[start]

    if start == end and end < N - 1:
        end += 1
        tmp += A[end]

print(ans)
