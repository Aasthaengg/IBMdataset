s=input()
k=int(input())
for i in range(min(k,len(s))):
  if s[i] != "1":
    print(s[i])
    break
else:
  print("1")