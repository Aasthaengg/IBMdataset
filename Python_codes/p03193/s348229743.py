N,H,W=map(int,input().split())
c=0
for _ in range(N):
    A,B=map(int,input().split())
    if A>=H and B>=W:
        c+=1
print(c)