s=input()

ans="No"
for i in range(len(s)):
  if s[i]=="C":
    for j in range(i+1,len(s)):
      if s[j]=="F":
        print("Yes")
        exit()
else:
  print(ans)
