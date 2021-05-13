from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())

counter = Counter(a)
sum_res = sum(a)

for i in range(q):
  b, c = map(int, input().split())
  
  sum_res -= b * counter[b]
  sum_res += c * counter[b]
  
  counter[c] += counter[b]
  counter[b] = 0
  
  print(sum_res)