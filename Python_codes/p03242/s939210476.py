n = str(input())

if n[0] == "9":
  ans = 100
elif n[0] == "1":
  ans = 900
  
if n[1] == "9":
  ans = ans + 10
elif n[1] == "1":
  ans = ans + 90

if n[2] == "9":
  ans = ans + 1
elif n[2] == "1":
  ans = ans + 9
  
print(ans)