def f(x):
    if x%2==0:
        res=x//2
    else:
        res=3*x+1
    return res



s=int(input())
a=[s]
for i in range(1,1000001):
    if f(a[i-1]) in a:
        print(i+1)
        break
    a.append(f(a[i-1]))