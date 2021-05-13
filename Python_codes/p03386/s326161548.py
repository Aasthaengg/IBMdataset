a,b,k=map(int, input().split())
k=min(k,b-a+1)
*al,=range(a,a+k)
*al2,=range(b-k+1,b+1)
ans=al+al2
ans=list(set(ans))
ans.sort()
for i in ans:print(i)

