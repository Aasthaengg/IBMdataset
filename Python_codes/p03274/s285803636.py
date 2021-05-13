n,k=map(int, input().split())
x=list(map(int, input().split()))

ans=float('inf')
for i in range(n-k+1):
    r=x[i]
    l=x[i+k-1]
    if r<0 and 0<=l:
        tmp_ans=min(2*abs(r)+l, abs(r)+2*l)
    elif 0<=r:
        tmp_ans=l
    else:
        tmp_ans=abs(r)
    ans=min(ans,tmp_ans)
print(ans)