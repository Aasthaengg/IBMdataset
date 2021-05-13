n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = []
x = []
for i in range(m):
    P, X = map(int, input().split())
    p.append(P)
    x.append(X)

for i in range(m):
    print(sum(t) - t[p[i]-1] + x[i])