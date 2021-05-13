# 解説みた
# わかったけど導けないなあ
n,k=map(int,input().split())
if k==0:
    print(n*n)
    exit()
cnt=0
for b in range(k+1,n+1):
    cnt+=(b-k)*(n//b)+max(0,n%b-k+1)
print(cnt)