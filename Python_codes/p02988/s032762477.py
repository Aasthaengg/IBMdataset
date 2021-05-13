N = int(input())
P = list(map(int,input().split()))
ans = 0
for i in range(1,N-1):
    a = P[i-1:i+2]
    a.sort()
    if P[i]==a[1]:
        ans += 1
print(ans)