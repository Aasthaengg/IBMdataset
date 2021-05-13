def f(k):
    cnt = 0
    while k%2 == 0:
        k //= 2
        cnt += 1
        # print(k)
        # print("-----")
    return cnt

n = int(input())
A = list(map(int, input().split()))
ans = 0

for a in A:
    if a%2 == 0:
        ans += f(a)
print(ans)