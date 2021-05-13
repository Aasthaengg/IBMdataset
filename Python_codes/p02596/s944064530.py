K = int(input())

num = 7%K

for i in range(K):
  if num%K ==0:
    print(i+1)
    break
  else:
    num = (num*10 + 7)%K
    
else:
  print(-1)