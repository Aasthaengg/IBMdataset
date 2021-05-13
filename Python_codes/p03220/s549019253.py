n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
dif = 10**10
ans = 0
for i in range(n):
    z = t-h[i]*0.006
    if dif>abs(a-z):
        dif = abs(a-z)
        ans = i+1
print(ans)