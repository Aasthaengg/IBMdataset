n = int(input())
amari = 0
i = 0
result = []
while i <= 40:
  if i ==0:
   hoge =  n % 2
   if hoge ==1:
      result.append(1)
      amari = 1
      i += 1
   else:
    result.append(0)
    i += 1
  else:
    hoge = n % (2**(i+1))
    if (amari + (-2)**(i)) % (2**(i+1)) == hoge:
      result.append(1)
      amari = amari + (-2)**(i)
      i += 1
    else:
      result.append(0)
      i += 1
      
result = result[::-1]
if n == 0:
  print(0)
else:
  s = ""
  check = False
  for r in result:
    if r == 0 and check == True:
      s += str(r)
    if r == 1:
      s += str(r)
      check = True
  print(int(s))
   
  

    
