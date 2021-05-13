# C - Rally

n = int(input())
x = list(map(int,input().split()))

c = []
x_ave = int(sum(x)/n)
s = 0
for i in range(n):
    s += (x[i]-x_ave)**2
c.append(s)
s = 0
for i in range(n):
    s += (x[i]-x_ave-1)**2
c.append(s)


print(min(c))
