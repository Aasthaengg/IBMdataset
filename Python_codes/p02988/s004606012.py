n = int(input())
p = list(map(int, input().split()))

cnt = 0

for i in range(n-2):
  pl = [p[j] for j in range(i, i+3)]
  if pl[0] < pl[1] <pl[2] or pl[2] < pl[1] < pl[0]:
    cnt += 1
  
print(cnt)