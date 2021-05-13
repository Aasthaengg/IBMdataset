A, B, C=map(int, input().split())

if B>=C:
  ans=B+C
else:
  ans=2*B
  C-=B
  ans+=min(A, C)
  C-=A
  if C>0:
    ans+=1
  
print(ans)