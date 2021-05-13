n=int(input())
li=list(map(int,input().split()))
li[0]-=1
for i in range(1,n-1):
    if li[i]>=li[i+1] and li[i]>li[i-1]:
        li[i]-=1
li2=sorted(li)
if li==li2:
    print("Yes")
else:
    print("No")