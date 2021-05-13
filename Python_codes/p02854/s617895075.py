from numpy import cumsum
n = int(input())
a = list(map(int, input().split()))

l = sum(a)
s = cumsum(a)
c = l*2
for i, x in enumerate(a):
    d = abs(s[i] * 2 - l)
    c = min(d, c)

print(c)
