X=int(input())
ans=1
for a in range(2,33):
  for b in range(2,11):
    if a**b>X:
      break
    if a**b<=X and a**b>ans:
      ans=a**b
print(ans)