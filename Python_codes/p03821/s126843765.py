n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

ans = 0
now = 0
for i in range(n-1,-1,-1):
    check = (A[i]+now)%B[i]
    if not check:
        continue
    tmp = B[i] - check
    ans += tmp
    now += tmp

print(ans)