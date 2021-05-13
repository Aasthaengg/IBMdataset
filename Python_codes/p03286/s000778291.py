N = int(input())
sec = [1,-2]
for i in range(2,32):
  if i%2 == 0:
    sec.append(sec[i-2]+pow(2,i))
  else:
    sec.append(sec[i-2]-pow(2,i))
#print(sec)
sec.reverse()
sec.append(0)
sec.append(0)
ans = []
for i in range(32):
  temp = 0
  if N >0 and sec[i] >0:
    if N>sec[i+2]:
      temp = 1
      #print(N,pow(-2,31-i))
      N -= pow(-2,31-i)
  elif N<0 and sec[i] <0:
    if N < sec[i+2]:
      temp = 1
      #print(N,pow(-2,31-i))
      N -= pow(-2,31-i)      
  ans.append(str(temp))

T = "".join(ans)
print(int(T))