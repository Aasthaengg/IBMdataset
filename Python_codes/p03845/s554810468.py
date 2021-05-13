from sys import stdin
def I(): return int(stdin.readline().rstrip())
def LI(): return list(map(int,stdin.readline().rstrip().split()))

n = I()
t = LI()
m = I()
p = []
x = []
for i in range(m):
    tmp = LI()
    p.append(tmp.pop(0)-1)
    x.append(tmp.pop(0))

for i in range(m):
    sum = 0
    for j in range(n):
        if j == p[i]:
            sum += x[i]
        else:
            sum += t[j]
    print(sum)