import sys

MOD = 1000000007

def union(x,y):
    if len(x)==1:
        if len(y)==1:
            return (1 if x[0]==y[0] else 0)
        else:
            return (1 if y[-1]>=x[0] else 0)
    if len(x)>1:
        if len(y)==1:
            return (1 if x[-1]>=y[0] else 0)
        else:
            return min(len(x),len(y))

n = int(input())
a = list(map(lambda x: int(x) % MOD, input().split()))
b = list(map(lambda x: int(x) % MOD, input().split()))
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
x[0] = 1
y[-1] = 1
z = 1

for i in range(1,n):
    if a[i-1]<a[i]:
        x[i] = 1
    else:
        x[i] = 0

for j in range(n-1, 0, -1):
    if b[j-1]>b[j]:
        y[j-1] += 1
    else:
        y[j-1] += 0

for i in range(n):
    if x[i] == 1 and y[i] == 0:
        if a[i] > b[i]:
            print(0)
            sys.exit()
    elif x[i] == 0 and y[i] == 1:
        if a[i] < b[i]:
            print(0)
            sys.exit()
    elif x[i] == 1 and y[i] == 1:
        if a[i] != b[i]:
            print(0)
            sys.exit()
    else:
        z *= min(a[i],b[i])
        z = z % MOD

print(z)
