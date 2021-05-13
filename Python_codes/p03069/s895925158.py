from itertools import accumulate
n = int(input())
s = list(input())
for i in range(n):
    if s[i] == "#":
        s[i] = 1
    else:
        s[i] = 0
cs = [0] + list(accumulate(s))
m = n
for i in range(n+1):
    num = cs[i] + (n-i)-(cs[n]-cs[i])
    m = min(m,num)
print(m)