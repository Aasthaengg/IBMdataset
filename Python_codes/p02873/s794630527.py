
s = str(input())
l = []
t = 0
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        l.append(s[t:i])
        t = i
else:
    l.append(s[t:len(s)])


def calc(n):
    tmp = 0
    for i in range(1,n+1):
        tmp += i
    return tmp

left = 0
right = 0
ans = 0

for i,sg in enumerate(l):
    if sg[0]=='>':
        if left < len(sg):
            ans -= left
            ans += calc(len(sg))
        else:
            ans += calc(len(sg)-1)
    else:
        ans += calc(len(sg))
        left = len(sg)

print(ans)