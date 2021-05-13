a = int(input())
c = 0
for i in range(a):
  z=list(map(int, input().split()))
  c+=max(z)-min(z)+1
print(c)