N = int(input())
p = list(map(int, input().split()))

i = 0
ans = 0
while i < N:
  if p[i] == i+1:
    if (i+1<N) and (p[i+1]==i+2):
      ans += 1
      i += 2
    else:
      ans += 1
      i += 1
  else:
    i += 1
print(ans)