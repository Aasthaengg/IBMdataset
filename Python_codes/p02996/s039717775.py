N=int(input())

arr=[list(map(int,input().split())) for i in range(N)]

brr=sorted(arr,key=lambda x:(x[1]))

time=0
work=0
count=0

for i in range(N):
    time=brr[i][1]
    work+=brr[i][0]
    if work<=time:
        count+=1
if count==N:
    print("Yes")
else:
    print("No")