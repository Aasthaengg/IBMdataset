from collections import Counter
N = int(input())
A = []
for i in range(N):
  A.append(int(input()))
  
c = Counter(A)
ans = 0
for i in c.items():
  if i[1] % 2 == 1:
    ans += 1
print(ans)