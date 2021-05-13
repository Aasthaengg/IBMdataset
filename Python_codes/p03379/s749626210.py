n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
h=n//2
a1=y[h]
a2=y[h-1]
for i in range(n):
    if x[i]<a1:
        print(a1)
    else:
        print(a2)