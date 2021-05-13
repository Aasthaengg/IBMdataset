n = int(input())
a = []
b = 0
for i in range(n):
  l,r=map(int, input().split())
  a.append((l,r))
  b = max(b,r)
  
acc = [0 for i in range(b+2)]
for l,r in a:
  acc[l] += 1
  acc[r+1] += -1
for i in range(b+1):
  acc[i+1] += acc[i]
print(sum(acc))
