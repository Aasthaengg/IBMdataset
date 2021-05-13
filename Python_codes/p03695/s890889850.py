N = int(input())
S = list(map(int,input().split()))

sp = [400,800,1200,1600,2000,2400,2800,3200]
rank = ["gray","brown","green","cyan","blue","yellow","orange","red","highest"]
cnt = [0]*len(rank)

import bisect as b

for score in S:
  cnt[b.bisect(sp,score)] += 1
  
mid = sum([1 for n in cnt[:-1] if n > 0])
t = cnt[-1]
max_amt = mid + t
min_amt = mid
if t > 0:
  min_amt = max(mid,1)
print(min_amt,max_amt)
#print(cnt)