n,k = map(int,input().split())
a = list(map(int,input().split()))
x = [0]*n
for ai in a:
  x[ai-1] += 1
x.sort()
print(sum(x[:n-k]))