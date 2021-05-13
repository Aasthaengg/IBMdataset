n, k = [int(i) for i in input().split()]
cnt = n
cnt_ = [0] * n
for _ in range(k):
  d = int(input())
  a = [int(i) for i in input().split()]
  for j in a:
    if cnt_[j - 1] == 0:
      cnt -= 1
      cnt_[j - 1] = 1
print(cnt)