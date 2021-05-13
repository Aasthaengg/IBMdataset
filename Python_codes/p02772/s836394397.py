n = int(input())
a = list(map(int,input().split()))
ans = "DENIED"
count = 0
for i in a:
  if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
    count += 1
if count == 0:
  ans = "APPROVED"
print(ans)