import sys
N = int(input())
a = list()
for i in range(N):
  a.append(int(input()))
i = 0
ans = 1
for _ in range(N):
  next_a = a[i]
  if(next_a == 2):
    print(ans)
    sys.exit()
  else:
    i = next_a-1
    ans += 1
print(-1)