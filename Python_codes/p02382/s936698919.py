import math
n=int(input())
x=list(map(int, input().split()))
y=list(map(int, input().split()))

p=[0]*3
Max=0
for i in range(3):
    for j in range(n):
        p[i]+=abs(x[j]-y[j])**(i+1)
        if abs(x[j]-y[j])>Max:
            Max=abs(x[j]-y[j])
            
    print('{:.5f}'.format(p[i]**(1/(i+1))))
print('{:.5f}'.format(Max))
