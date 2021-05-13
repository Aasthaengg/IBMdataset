from operator import itemgetter
n = int(input())
lst = [0] * n
for i in range(n):
  lst[i] = tuple(map(int, input().split()))
lst.sort(key=itemgetter(1))
t = 0
for i in range(n):
  t += lst[i][0]
  if t > lst[i][1]:
    print('No')
    exit()
print('Yes')