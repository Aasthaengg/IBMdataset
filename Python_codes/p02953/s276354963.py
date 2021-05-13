n = int(input())
a = list(map(int, input().split()))
p = 0
for i in a:
  if p > i:
    print('No')
    exit()
  if p < i:
    p = i - 1
print('Yes')
