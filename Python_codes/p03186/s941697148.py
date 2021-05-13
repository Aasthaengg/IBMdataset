A,B,C=map(int,input().split())
ans=0

if B>=C:
    print(C+B)
    exit()

ans+=B*2
C-=B

if A>=C-1:
    print(ans+C)
else:
    print(ans+A+1)