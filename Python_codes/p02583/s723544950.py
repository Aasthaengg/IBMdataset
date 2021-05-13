N = int(input())
L = list(map(int, input().split()))
ans = 0

for i in range(N):
  for j in range(N):
    for k in range(N):
      if L[i] < L[j] < L[k]:
        if L[i] + L[j] > L[k]:
          ans += 1

print(ans)