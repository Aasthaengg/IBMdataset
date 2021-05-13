A,B,C=map(int,input().split())

if A>=C:
  ans = C+B
else:
  if B >=C-A:
    ans= B+C
  else:
    ans= B+A+B+1 
          
print(ans)