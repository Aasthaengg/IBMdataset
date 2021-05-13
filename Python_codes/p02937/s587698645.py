key= list('abcdefghijklmnopqrstuvwxyz')
value=[[] for i in range(26)]
d = dict(zip(key,value))
import bisect    
s = input()
s = list(s)
n = len(s)
ans = 0
for i in range(len(s)):
    d[s[i]].append(i+1)
st = set(s)
t = input()
t = list(t)
b = 0
for i in range(len(t)):
    if t[i] in st:
        p = bisect.bisect(d[t[i]],b) 
        if p < len(d[t[i]]):
            b = d[t[i]][p]
        else:
            b = d[t[i]][0]
            ans += n
    else:
        ans = -1
        break
if ans != -1:
    ans += b
print(ans)