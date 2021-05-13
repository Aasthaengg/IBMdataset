N,M,X=map(int,input().split())
A=list(map(int,input().split()))
cnt_1=0
cnt_2=0
for i in range(M):
    if A[i]<X:
        cnt_1+=1
    else:
        cnt_2+=1
print(min(cnt_1,cnt_2))