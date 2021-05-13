N=int(input())
a=list(map(int,input().split()))
two=0
four=0
odd=0

for i in range(N):
    cnt=0
    if a[i]%2==0:
        cnt+=1
    if a[i]%4==0:
        cnt+=1
    
    if cnt==0:
        odd+=1
    elif cnt==1:
        two+=1
    else:
        four+=1

if odd>four:
    if two==0:
        if odd==four+1:
            print("Yes")
            exit()
    print("No")
else:
    print("Yes")