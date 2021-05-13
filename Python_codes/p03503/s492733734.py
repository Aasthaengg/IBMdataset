n=int(input())
S=[int(input().replace(' ',''),2) for _ in range(n)]
C=[list(map(int,input().split())) for _ in range(n)]
A=[]
for i in range(1,2**10):
    ans=0
    for j in range(n):
        cnt=bin(S[j]&i).count('1')
        ans+=C[j][cnt]
    A.append(ans)
print(max(A))       