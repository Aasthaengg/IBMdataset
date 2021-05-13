n = int(input())
lr = []
for i in range(n):
  array = list(map(int,input().split()))
  lr.append(array)
ans = 0
for i in lr:
  ans += abs(i[0]-i[1])+1
print(ans)