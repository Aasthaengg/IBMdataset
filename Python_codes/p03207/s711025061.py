n = int(input())
ar = []
for _ in range(n):
  ar.append(int(input()))

print(sum(ar)-max(ar)//2)