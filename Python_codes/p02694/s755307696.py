X = int(input())
En=100
N=0

while En<X:
  En+=En//100
  N+=1

print(N)