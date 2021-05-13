N=int(input())
for i in range(N,0,-1):
  if int(i**0.5)**2==i:
    print(i)
    break