from collections import Counter
n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
numSum = 0
for i in count.values():
  numSum += i*(i-1)//2

for i in a:
  print(numSum - (count[i]-1))