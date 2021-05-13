n, k = map(int,input().split())
a = [0] + list(map(int,input().split()))

s = []
ord = [-1] *(n+1)
c = 0

v = 1
while ord[v] == -1:
    ord[v] = len(s)
    s.append(v)
    v = a[v]

c = len(s) - ord[v]
l = ord[v]

if k < l:
    print(s[k])
else:
    k -= l
    k %= c
    print(s[l+k])
