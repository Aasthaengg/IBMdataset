W,a,b=map(int,input().split())
Max=max(a,b)
Min=min(a,b)

ans=Max-(Min+W)
if ans<0:
    ans=0
print(ans)