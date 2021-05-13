# input
n = int(input())
v = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

# main
for i in range(n):
  v[i] -= c[i]

ans = 0
for i in range(n):
  if v[i] >= 0:
    ans += v[i]
    
# output
print(ans)