L, R, d = map(int,input().split())

ans = []

for i in range(L, R + 1):
  if i % d == 0:
    ans.append(i)

print(len(ans))