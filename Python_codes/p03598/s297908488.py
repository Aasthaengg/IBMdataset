n=int (input())
k=int (input())
x= list(map(int, input().strip().split()))
t=0
for i in range(n):
    #print(x[i])
    a=2*x[i]
    b=abs(2*(k-x[i]))
    #print(a,b)
    t+=min(a,b)
print(t)