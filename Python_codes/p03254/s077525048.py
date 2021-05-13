n,x = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0
for i in a:
    if x>=i:
        ans+=1
        x-=i
print(ans-1 if ans==n and x>0 else ans)