N = int(input())
H = list(map(int, input().split()))

i, j = 0, 1
count = 0
ans = 0
while j < N:
  if H[i] >= H[j]:
    count += 1
    i += 1
    j += 1
  else:
    ans = max(ans, count)
    count = 0
    i = j
    j += 1
ans = max(ans, count)
print(ans)