n = int(input())
lst = list(map(int, input().split()))
mcnt = 0
for i in range(n):
  if lst[i] < 0:
    mcnt += 1
if 0 in lst or mcnt % 2 == 0:
  print(sum(list(map(abs, lst))))
  exit()
m = min(lst, key=abs)
print(sum(list(map(abs, lst))) - 2 * abs(m))