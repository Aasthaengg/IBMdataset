def dist(s1,s2):
  return abs(s1[1]-s2[1]) + abs(s1[2]-s2[2])

N=int(input())
now = (0,0,0)
for i in range(N):
  next_ = list(map(int,input().split()))
  if dist(now,next_)<=next_[0]-now[0] and dist(now,next_) % 2 == (next_[0]-now[0])%2:
    now = next_
    continue
  else:
    print('No')
    exit()
print('Yes')