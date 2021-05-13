n = int(input())

total = 0
for i in range(n):
  s,e = list(map(int,input().strip().split()))
  total += (e-s+1)

print(total)