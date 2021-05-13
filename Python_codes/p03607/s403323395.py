import collections
N = int(input())
ans = [0] * N

for i in range(N):
  ans[i] = int(input())
  
C = collections.Counter(ans)
count = 0
for i in C.values():
  if i % 2 == 1:
    count += 1
  
print(count)