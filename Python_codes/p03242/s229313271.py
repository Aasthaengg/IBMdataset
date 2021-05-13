num=str(input())
ans = ""
for i in range(3):
  if num[i]=="1":
    ans+="9"
  elif num[i]=="9":
    ans+="1"
  else:
    ans += num[i]
print(ans)