n = int(input())
s1=input()
s2=input()
mod = 10**9+7
l = []
for i in range(0,n-1):
    if s1[i] != s1[i+1]:
        if s1[i] != s2[i]:
            l.append(0)
        else:
            l.append(1)
if s1[n-1]==s2[n-1]:
    l.append(1)
else:
    l.append(0)
if l[0]:
    res = 3
else:
    res = 6

for i in range(1,len(l)):
    if l[i-1] and l[i]:
        res *= 2
    elif l[i-1] and  not l[i]:
        res *= 2
    elif not l[i-1] and not l[i]:
        res *= 3

print(res % mod)