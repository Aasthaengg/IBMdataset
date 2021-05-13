N=int(input())

for i in reversed(range(1,N+1)):
  if i**0.5==int(i**0.5):
    print(i)
    break