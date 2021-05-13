n = int(input())
P = ["D"] + list(map(int,input().split()))

ans = 0
for i in range(1,n):
    if P[i] == i:
        ans += 1
        P[i+1] = P[i]
if P[-1] == n:
    ans += 1
print(ans)