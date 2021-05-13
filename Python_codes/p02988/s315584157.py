import copy
n = int(input())
s = list(map(int, input().split()))

count = 0

for i in range(n - 2):
  t = copy.copy(s[i:i + 3])
  if(s[i + 1] == sorted(t)[1]):
    count += 1

print(count)
