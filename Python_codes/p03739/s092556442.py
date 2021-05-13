N = int(input())
A = list(map(int, input().split()))
sm1=0
sm2=0
cnt=0
cnt2=0

for i in range(N):
    sm1+=A[i]
    if i%2==1:
        if sm1>=0:               
            cnt+=sm1+1
            sm1=-1
    else:
        if sm1<=0:               
            cnt+=sm1*-1+1
            sm1=1

for i in range(N):
    sm2+=A[i]
    if i%2==1:
        if sm2<=0:
            cnt2+=sm2*-1+1
            sm2=1
    else:
        if sm2>=0:
            cnt2+=sm2+1
            sm2=-1
print(min(cnt,cnt2))