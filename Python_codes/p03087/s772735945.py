#c
N,Q = map(int,input().split())
S=input()

old=S[0]
cnt=0
rui = [0]*N
for i in range(1,N):
    now = S[i]
    if old=="A" and now=="C":
        cnt+=1
    old=now
    rui[i]=cnt    

for i in range(Q):
    l,r = map(int,input().split())
    print(rui[r-1]-rui[l-1])