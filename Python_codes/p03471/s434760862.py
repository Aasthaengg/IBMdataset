n,y  = map(int, input().split())

ans = "-1 -1 -1"
for i in range(n+1):
  for j in range(n-i+1):
    k = n-i-j
    if 10000*i+5000*j+1000*k == y:
      ans = str(i)+" "+str(j)+" "+str(k)
      break

print(ans)