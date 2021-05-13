w = sorted(input())
if len(w)%2 == 1:
  print("No")
  exit()
for i in range(len(w)//2)[::2]:
  if w[i] != w[i+1]:
    print("No")
    exit()
print("Yes")