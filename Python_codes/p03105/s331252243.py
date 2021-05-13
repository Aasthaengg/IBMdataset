#120 a
a,b,c=map(int,input().split())
ans=int(b/a)
if ans>c:
    ans=c
print(ans)