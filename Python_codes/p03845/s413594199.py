n = int(input())
t = list(map(int,input().split()))
m = int(input())
p = [list(map(int,input().split())) for i in range(m)]
k = 0
tmp = t[:]
for i in range(m):
    k = p[i][0]
    t[k-1] = p[i][1]
    print(sum(t))
    t[k-1] = tmp[k-1]