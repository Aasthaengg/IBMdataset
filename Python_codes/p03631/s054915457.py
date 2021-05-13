N=list(input())
for i in range(len(N)//2+1):
  #print(N[i],N[len(N)-i-1])
  if N[i]!=N[len(N)-i-1]:
    print("No")
    break
else:
  print("Yes")
