from collections import Counter
n = int(input())
a = list(map(int, input().split()))

count = Counter(a)

ans = 0
for i in count.items():
  if i[1] < i[0]: ans += i[1]
  else: ans += abs(i[1]-i[0])
    
print(ans)