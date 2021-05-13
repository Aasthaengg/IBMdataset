D = int(input())
c = list(map(int, input().split()))
s = []

t = [0]*D
v = [0]*D
d = [0]*26

for i in range(D):
    S = list(map(int, input().split()))
    s.append(S)

for i in range(D):
    t[i] = int(input())

now = 0

for i in range(D):
    now += s[i][t[i]-1]
    d[t[i]-1] = i+1
    for j in range(26):
        now -= c[j] * (i+1-d[j])
    v[i] = now
    print(v[i])