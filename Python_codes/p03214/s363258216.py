
N = int(input())

a = list(map(int,input().split()))

s = sum(a) / N
m = float("inf")

ans = 0
for i in range(N):
  if abs(a[ans]-s) > abs(a[i]-s):
    ans = i
    
print (ans)