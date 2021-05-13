import bisect
s = input()
t = input()
u = s
while len(s) <= len(t):
    s += u
p = [[] for k in range(26)]
for k in range(len(s)):
    p[ord(s[k])-97].append(k)
for e in p:
    e.append(10**6)
ans = 0
now = -1
for e in t:
#    print(p[ord(e)-97][bisect.bisect_left(p[ord(e)-97],now)])
    if len(p[ord(e)-97]) == 1:
        print(-1)
        exit(0)
    q = p[ord(e)-97][bisect.bisect_right(p[ord(e)-97],now)]
    if q == 10**6:
        ans += len(s)-now+p[ord(e)-97][0]
        now = p[ord(e)-97][0]
    else:
        ans += q-now
        now = q
print(ans)
