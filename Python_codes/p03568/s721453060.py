import functools
import operator

n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(3**n):
    p=i
    c=[]
    for j in range(n):
        p,b=p//3,p%3
        if b == 0:
            c.append(a[j]-1)
        elif b==1:
            c.append(a[j])
        else:
            c.append(a[j]+1)
    x = functools.reduce(operator.mul, c)
    if x%2 == 0:
        ans += 1
print(ans)