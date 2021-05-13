N=input()
ans=0
for i in range(2**((len(N)-1))):
  b = N[len(N)-1]
  for j in range(len(N)-1):
    if (i>>j)&1==1:
      ans += int(b)
      b = N[len(N)-2-j]
    else:
      b = N[len(N)-2-j] + b
  else:
    ans += int(b)
print(ans)  