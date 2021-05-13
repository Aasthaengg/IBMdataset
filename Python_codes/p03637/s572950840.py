n=int(input())
a=list(map(int,input().split()))
num=[0,0,0]
for i in range(n):
    if a[i]%4==0:
        num[2]+=1
    elif a[i]%2==0:
        num[1]+=1
    else:
        num[0]+=1
if num[1]==0:
    if num[0]>num[2]+1:
        print("No")
    else:
        print("Yes")
elif num[0]>num[2]:
    print("No")
else:
    print("Yes")
