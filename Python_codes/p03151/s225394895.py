N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
  print(-1)
  quit()

ans = 0
diff = 0
larger = []
for a, b in zip(A, B):
  if a < b:
    ans += 1
    diff += b - a
  else:
    larger.append(a - b)

larger.sort(reverse=True)
for l in larger:
  if diff > 0:
    diff -= l
    ans += 1
  else:
    break

print(ans)