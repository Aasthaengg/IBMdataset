n = int(input())
P = list(map(int, input().split()))
count = 0
for i in range(1, n + 1):
  if P[i - 1] != i:
    count += 1
print("YES" if count <= 2 else "NO")