d = int(input())
c = list(map(int, input().split()))
s = [[0]*26 for _ in range(d)]

for i in range(d):
    s[i] = list(map(int, input().split()))

v = [0]*d
for i in range(d):
    v[i] = int(input())

lday = [0]*26
sat = 0
for i in range(d):
    lday[v[i]-1] = i+1
    sat = sat + s[i][v[i]-1]
    for j in range(26):
        sat = sat - c[j]*(i+1 - lday[j])
    print(sat)