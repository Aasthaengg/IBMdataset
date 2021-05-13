n, k = map(int, input().split())
a = list(map(int, input().split()))

s = []
o = [-1] * (n + 1)
count = 0

v = 1
while o[v] == -1:
    o[v] = count
    s.append(v)
    v = a[v-1]
    count += 1

l = o[v]
c = len(s) - o[v]
    
if k < l:
    print(s[k])
else:
    k -= l
    k = k % c
    print(s[l+k])
