n = int(input())
ans = [0] * 10050
for i in range(1,101):
  for j in range(1,101):
    for k in range(1,101):
      v = i*i+j*j+k*k+i*j+j*k+k*i
      if v<10050:
        ans[v]+=1
for i in range(n):
  print(ans[i+1])