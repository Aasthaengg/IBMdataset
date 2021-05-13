N = int(input())
a = list(map(int, input().split())) 
ans = 0

for i in range(0,N-1):
  ans = ans + sorted(a)[i+1] - sorted(a)[i]
print (ans)