n = int(input())
d = {}
for i in range(n):
    s ,p = input().split()
    p = int(p)
    if not(s in d):
        d[s] = {}
    d[s][p*-1] = i+1
for i in sorted(d.keys()):
    for j in sorted(d[i].keys()):
        print(d[i][j])
