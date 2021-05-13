N=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)
ansa,ansb=0,0
for i in range(N):
    if i%2==0:
        ansa+=a[i]
    else:
        ansb+=a[i]
print(ansa-ansb)
