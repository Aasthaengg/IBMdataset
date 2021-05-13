r=input().split()
K=int(r[0])
X=int(r[1])
S=""
for i in range(2*K-1):
    ans=X-K+i+1
    if -1000000<=ans<=1000000:
        S+=str(ans)+" "
print(S.rstrip())