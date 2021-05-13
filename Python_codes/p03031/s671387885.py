n,m = map(int,input().split())
s = [0] * m
ans = 0
for i in range(m):
    s[i] = list(map(int,input().split()))
    s[i] = s[i][1:]
p = list(map(int,input().split()))
for k in range(2**n):
    a = format(k,'0'+str(n)+'b')
    t = True
    for i in range(m):
        if sum(a[j-1] == '1' for j in s[i])%2 != p[i]:
            t = False
            break
    ans += t
print(ans)
