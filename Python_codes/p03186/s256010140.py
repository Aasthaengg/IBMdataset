(A,B,C)=[int(z) for z in input().split(" ")]
ans=0
if B>=C:
  ans=B+C
else:
  ans+=2*B
  C-=B
  if A+1>C:
    ans+=C
  else:
    ans+=A+1

print(ans)