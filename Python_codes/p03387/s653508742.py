A,B,C = sorted(map(int,input().split()))
ans = 0

for n in range(50):
  if A==B==C:
    break
  elif A<C and B<C:
    A+=1
    B+=1
    ans+=1
  elif A<C and B==C:
    A+=2
    ans+=1
  else:
    B+=1
    C+=1
    ans+=1
    
print(ans)