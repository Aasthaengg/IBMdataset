n = int(input())
t = list(map(int,input().split()))
m = int(input())
p = []
x = []
for i in range(m):
    a,b = map(int,input().split())
    p.append(a)
    x.append(b)

for i in range(m):
    s = list(t)
    j = p[i] - 1
    s[j] = x[i]
    print(sum(s))