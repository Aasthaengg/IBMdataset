N=int(input())
A=list(map(int, input().split()))
arai=sum(A)
ans=10**19
sunuke=0
for a in range(N-1):
  sunuke+=A[a]
  arai-=A[a]
  if ans>abs(arai-sunuke):
    ans=abs(arai-sunuke)
print(ans)
