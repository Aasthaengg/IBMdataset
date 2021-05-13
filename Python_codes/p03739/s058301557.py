N=int(input())
A=list(map(int,input().split()))
cnt_1=0
cnt_2=0
sum_1=0
sum_2=0

for i in range(N):
    sum_1+=A[i]
    if i%2==1:
        if sum_1<=0:
            cnt_1+=1-sum_1
            sum_1=1
    else:
        if sum_1>=0:
            cnt_1+=sum_1+1
            sum_1=-1

for i in range(N):
    sum_2+=A[i]
    if i%2==1:
        if sum_2>=0:
            cnt_2+=sum_2+1
            sum_2=-1
    else:
        if sum_2<=0:
            cnt_2+=1-sum_2
            sum_2=1

print(min(cnt_1,cnt_2))