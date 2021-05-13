n,k = map(int,input().split())
s = input()
c = []
buf = 1
for i in range(n-1):
    if s[i]==s[i+1]:
        buf += 1
    else:
        c.append(buf)
        buf = 1
c.append(buf)
n = len(c)
l = min(n,2*k+1)
ans = buf = sum(c[:l])
ind = 0
for i in range(n-l):
    buf = buf-c[i]+c[i+l]
    if ans<buf:
        ind = i+1
        ans = buf
ans -= 1
for i in range(n):
    if ind<=i<ind+l:
        continue
    ans += c[i]-1
print(ans)