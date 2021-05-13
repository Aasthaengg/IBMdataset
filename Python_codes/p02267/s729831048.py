N = input()
S = set(map(int, input().split()))
Q = input()
T = set(map(int, input().split()))

ans = 0
for t in T:
  if t in S:
    ans += 1
print(ans)
