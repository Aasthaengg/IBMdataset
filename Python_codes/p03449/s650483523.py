n = int(input())
a = []
ans = 0
for _ in range(2):
    s = [0]
    ai = list(map(int,input().split()))
    for i in range(n):
        s.append(s[i]+ai[i])
    a.append(s)
for i in range(n+1):
    j = a[0][i]
    k = a[1][n]-a[1][i-1]
    ans = max(ans,j+k)
print(ans)