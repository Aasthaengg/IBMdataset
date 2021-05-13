import copy
n=int(input())
x=list(map(int,input().split()))

y=copy.copy(x)
y.sort()

left=y[n//2-1]
right=y[n//2]

for i in range(n):
    if x[i]<=left:
        print(right)
    else:
        print(left)
