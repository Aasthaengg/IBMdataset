a = input()
ans =""
for i in a:
  if i =="1":
    ans +="9"
  elif i =="9":
    ans +="1"
  else:
    ans += i
print(ans)