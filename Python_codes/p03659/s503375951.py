N = int(input())
L = list(map(int, input().split()))
total = sum(L)

# e.g.) Sunuke takes i cards from the top (1 <= i <= N-1)
# Sunuke's score is sum(L[:i]) ... L[i] -> + L[i+1]
# Racoon's score is sum(L[i:]) ... sum(L) - L[i] -> L[i+1]


sunuke = 0
ans = 2**64-1
for i in range(N-1):
  sunuke += L[i]
  racoon = total - sunuke
  ans = min(ans, abs(sunuke - racoon))
print(ans)
