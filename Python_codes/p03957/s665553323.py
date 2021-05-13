s = input()
n = len(s)
for i in range(n):
  if s[i]=="C":
    for j in range(i,n):
      if s[j]=="F":
        print("Yes")
        exit()
else:
  print("No")