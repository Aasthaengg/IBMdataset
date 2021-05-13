N=int(input())

for i in range(10):
 if N>1000:
  N-=1000
 if N<1000:
  break

print(1000-N)