N=int(input())
a=list(map(int,input().split()))
t=0
for i in a[1:]:
    t^=i
print(t,end=" ")
for i in range(N-1):
    t^=a[i]
    t^=a[i+1]
    print(t,end=" ")