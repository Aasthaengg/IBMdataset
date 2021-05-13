n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

l = []
for i in range(n):
  x = sum(a1[:i+1]) + sum(a2[i:])
  l.append(x)
  
print(max(l))