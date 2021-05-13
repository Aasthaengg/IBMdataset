n=int(input())
a=list(map(int,input().split()))

def choose2(n):
  if n <= 1:
    return 0
  return n*(n-1)//2

inp = [0]*(n+1)
for i in range(n):
  inp[a[i]] += 1

total = 0
for i in range(n+1):
  total += choose2(inp[i])

for i in range(n):
  count = total - choose2(inp[a[i]]) + choose2(inp[a[i]]-1)
  print(count)
