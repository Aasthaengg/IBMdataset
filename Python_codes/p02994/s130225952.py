N, L = map(int, input().split())

if L >= 1:
  eat = L
elif L+N-1 <= -1:
  eat = L+N-1
else:
  eat = 0

taste = eat*(-1)
for i in range(N):
  taste += L+i

print(taste)