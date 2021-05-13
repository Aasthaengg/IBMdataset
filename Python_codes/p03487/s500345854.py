from collections import Counter

N = int(input())
As = list(map(int, input().split()))

rlt = 0
dic = Counter(As)

for k in dic:
  if dic[k] < k:
    rlt += dic[k]
  elif dic[k] > k:
    rlt += dic[k] - k
    
print(rlt)
