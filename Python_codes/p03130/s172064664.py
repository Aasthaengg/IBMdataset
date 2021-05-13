lis = []
for i in range(3):
  lis = lis + list(map(int, input().split()))
#print(lis)

ans = "YES"

for i in range(4):
  a = lis.count(i+1)
  if a >= 3:
    ans = "NO"
    break
print(ans)