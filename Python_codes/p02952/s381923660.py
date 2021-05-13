N = int(input())
res = 0
for i in range(N):
  if len(str(i + 1)) % 2 == 1:
    res += 1
print(res)