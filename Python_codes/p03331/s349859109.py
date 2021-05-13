ans=float("INF")
n=int(input())

s=0
for i in range(1,n//2+1):
  ans=min(sum(list(map(int,list(str(i)))))+sum(list(map(int,list(str(n-i))))),ans)
print(ans)