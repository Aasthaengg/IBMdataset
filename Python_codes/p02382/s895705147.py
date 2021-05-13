n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
a = [0]*4
for i in range(n):
    a[0] += abs(x[i]-y[i])
    a[1] += abs(x[i]-y[i])**2
    a[2] += abs(x[i]-y[i])**3
    a[3] = max(a[3],abs(x[i]-y[i]))
a[1] = a[1]**(1/2)
a[2] = a[2]**(1/3)
for i in range(4):
    print('%f' % a[i])
