n, k = map(int, input().split())
b = [0]*n
for _ in range(k):
  a = int(input())
  c = list(map(int, input().split()))
  for i in c:
    b[i-1] = 1  
print(b.count(0))