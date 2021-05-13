team=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
ans=0
for i in range(team):
   ans+=l[i*2+1]
print(ans)