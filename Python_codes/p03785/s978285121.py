n, c, k = list(map(int, input().split()))
t = [int(input()) for i in range(n)]
t.sort()

limit = t[0] + k
num = 1
cnt = 1
for i in range(1, n):
  if limit < t[i] or num == c:
    num = 1
    limit = t[i] + k
    cnt += 1
  
  else:
    num += 1
print(cnt)