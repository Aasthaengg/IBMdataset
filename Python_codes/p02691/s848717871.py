from collections import defaultdict
n = int(input())
a = list(map(int, input().split())) 
cnt = 0
c = defaultdict(int)
for i in range(n):
  c[i+1-a[i]] += 1
for i in range(n):
  cnt += c[a[i]+i+1]
print(cnt)