n=int(input())
ans=0
for i in range(25):
  for j in range(14):
    if 4*i + 7*j ==n:
      ans=1
print("Yes" if ans==1 else "No")