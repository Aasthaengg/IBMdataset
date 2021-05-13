ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

aa=sorted(nl())[::-1]

ans = 0
if(aa[1]-aa[2])%2==1:
  aa[0]+=1
  aa[1]+=1
  ans=1
ans+=(aa[1]-aa[2])//2
ans += aa[0]-aa[1]
print(ans)
