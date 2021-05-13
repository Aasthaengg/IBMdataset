O=input()
E=input()
ans=""
for i in range(len(O)):
  try:
    ans+=O[i]+E[i]
  except:
    ans+=O[i]
print(ans)