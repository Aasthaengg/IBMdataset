n=int(input())
ls=list(map(int,input().split()))
copy=[0]*n
for i in range(n):
    copy[ls[i]-1]=i+1
for i in copy:
       print(i,end=" ")