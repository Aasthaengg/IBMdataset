N = int(input())
A = list(map(int,input().split()))
Flag = True
for x in A:
  if x%2 != 1:
    Flag = False
    break
if Flag:
  print(0)
  exit()
ans = 0
for x in A:
  while x%2 == 0:
    ans += 1
    x = x//2
print(ans)