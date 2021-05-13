def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

X = cin()
cnt = 0
i = 0
while(i < X):
    cnt += 1
    i += cnt
print(cnt)