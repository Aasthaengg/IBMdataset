N = int(input())
A = list(map(int,input().split()))
c = 0
for s in A:
  while True:
    if s % 2 == 1:
      break
    s //= 2
    c+=1
print(c)