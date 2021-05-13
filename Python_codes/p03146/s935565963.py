s = int(input())

answer = 1
an = {1:s}
i = 2
while(True):
  if an[i-1]%2 == 0:
    if (an[i-1]//2) in an.values():
      answer = i
      break
    else :
      an[i] = an[i-1]//2
  else :
    if (3*an[i-1]+1) in an.values():
      answer = i
      break
    else :
      an[i] = 3*an[i-1]+1
  i += 1  
      
print(answer)