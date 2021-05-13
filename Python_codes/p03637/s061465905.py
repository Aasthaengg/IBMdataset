n=int(input())
a=list(map(int,input().split()))
nn=[0,0,0]
for i,v in enumerate(a):
    tmp=0
    while v%2==0:
        v//=2
        tmp+=1
    nn[min(tmp,2)]+=1
if nn[1]:
    if nn[0]>(n-nn[1])//2:
        print("No")
    else:
        print("Yes")
else:
    if nn[0]>(n+1)//2:
        print("No")
    else:
        print("Yes")