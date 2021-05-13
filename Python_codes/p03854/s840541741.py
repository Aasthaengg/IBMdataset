st = input()
S = st[::-1]
words ={"remaerd","resare","maerd","esare"}

lenT = 0
flag = 0
ans = "NO"

while flag < 5:
  for i in range(5, 8):
    if S[0:i] in words:
      S = S[i:]
      flag = 0
      
    elif S == "":
      flag = 5
      ans = "YES"
      break
    else:
      flag += 1
    
print(ans)