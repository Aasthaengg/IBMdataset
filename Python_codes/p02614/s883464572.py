n, w, k = [int(i) for i in input().split()]
l = []
cnt = 0
for _ in range(n):
  l.append(list(input()))
import itertools
for w_ in itertools.product((True, False), repeat=w):
  for n_ in itertools.product((True, False), repeat=n):
    cnt_ = 0
    for i in range(w):
      for j in range(n):
        if w_[i] and n_[j] and l[j][i] == '#':
          cnt_ += 1
    if cnt_ == k:
      cnt += 1
print(cnt)