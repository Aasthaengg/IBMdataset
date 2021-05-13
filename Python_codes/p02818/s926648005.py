A,B,K=map(int,input().split())
if A>=K:
    c=A-K
    d=B
elif A==0 and B>=K:
    c=0
    d=B-K
elif A+B<=K:
    c=0
    d=0
else:
    d=B-(K-A)
    c=0
print(str(c)+' '+str(d))