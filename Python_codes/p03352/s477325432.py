X=int(input())

MAX=0
for i in range(1,int(X**.5)+3):
  for j in range(2,10):
    if i**j<=X:
      if MAX < i**j:
        MAX = i**j
    else:
      break

print(MAX)