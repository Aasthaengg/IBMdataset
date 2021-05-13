N, x = map(int, input().split())
a = list(map(int, input().split()))
p = x
a.sort()
count = 0

for i in a:
  if x - i >= 0:
    x -= i
    count += 1
if x > 0 and count != 0  and p > sum(a):
  count -= 1
print(count)