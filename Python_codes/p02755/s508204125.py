A,B=list(map(int, input().split()))
for i in range(B*10,(B+1)*10):
  if int(i*0.08)==A:
    print(i)
    break
else:
  print(-1)