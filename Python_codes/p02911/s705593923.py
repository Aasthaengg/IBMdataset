N,K,Q=map(int,input().split())
score=[K-Q]*N
for i in range(Q):
    a=int(input())
    score[a-1]+=1
for i in range(N):
    if score[i]<=0:
        print("No")
    else:
        print("Yes")