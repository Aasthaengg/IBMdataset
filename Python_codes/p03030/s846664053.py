n = int(input())
r = []
for i in range(n):
    s,p = input().split()
    p = -int(p)
    r.append([s,p,i])
a = sorted(r)
for i in range(n):
    print(a[i][2]+1)
