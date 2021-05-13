from math import ceil as c
input()
m=M=2
for b in map(int,input().split()[::-1]):
  m = c(m/b)*b
  M = c((M+1)/b)*b-1
  if m > M:
    print(-1)
    exit()
print(m,M)