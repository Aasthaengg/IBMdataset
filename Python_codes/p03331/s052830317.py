N = int(input())
ans = N

for i in range(1,N):
  j = N-i
  ist = str(i)
  jst = str(j)
  iarray = list(map(int ,ist))
  jarray = list(map(int ,jst))
  isum = sum(iarray)
  jsum = sum(jarray)
  if isum + jsum < ans:
    ans = isum + jsum
print(ans)
    
    
  
