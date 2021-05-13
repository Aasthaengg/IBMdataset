A,B,K=map(int,input().split())
if B==A:
    print(A)
    exit()
K=min(K,B-A)
ans=set()
for i in range(K):
    ans.add(A+i)
    ans.add(B-i)
ans=list(ans)
ans=sorted(ans)
for i in ans:
    print(i)