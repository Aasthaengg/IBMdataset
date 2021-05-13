N=int(input())
S=list(map(int,input().split()))
c=0
an=0
for i in range(N-1):
  if S[i]>=S[i+1]:
    an+=1
  else:
    c=max(an,c)
    an=0
print(max(c,an))