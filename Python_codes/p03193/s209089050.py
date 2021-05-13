N,H,W=map(int,raw_input().split())
A=[]
B=[]
Ans=0
for i in range(N):
    ab=map(int,raw_input().split())
    if ab[0]>=H and ab[1]>=W:
        Ans+=1

print Ans