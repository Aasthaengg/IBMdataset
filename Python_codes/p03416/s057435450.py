A,B = map(int,input().split())
c = 0
for i in range(A,B+1):
  s = str(i)
  k = True
  for j in range(len(s)//2):
    if s[j] != s[(j+1)*-1]: 
      k = False
      break
  if k:
      c+=1     
print(c)