d = int(input())
c = list(map(int,input().split()))
s = []
t = [0]*d
for i in range(d):
    s.append(list(map(int,input().split())))
for i in range(d):
    t[i] = int(input())-1
v = 0
x = [1]*26
for i in range(d):
    x[t[i]] *= 0
    v += s[i][t[i]]
    for j in range(26):
        v -= c[j]*x[j]
        x[j] += 1
    print(v)