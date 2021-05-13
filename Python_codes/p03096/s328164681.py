import sys
DBG =  not True
R = 1000000007
MAXN = 200000
n = int(input())
c = []
for i in range(n):
    c.append(int(input()))
tot = 1
s = [0] * (MAXN+1)
for i in range(n):
    if i > 0 and c[i] == c[i-1]:
        continue
    x = s[c[i]]
    tot = (tot + x) % R
    s[c[i]] = tot
    if DBG:
        print("i {} sci {} tot {} newt {}".format(i,x,s[c[i]],tot))
        print(s)
print(tot)
