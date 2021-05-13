n=int(input())
a=list(map(int,input().split()))
cnt1=0
cnt2=0
cnt4=0
if n==2:
    if a[0]*a[1]%4==0:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
for i in range(n):
    if a[i]%4==0:
        cnt4+=1
    elif a[i]%2==0:
        cnt2+=1
    else:
        cnt1+=1
if cnt1 == 0 or (cnt2 == 0 and cnt4+1 >= cnt1) or (cnt2 >= 1 and cnt4 >= cnt1):
    print("Yes")
else:
    print("No")

