import sys
readline = sys.stdin.readline

N = int(readline())
L = list(map(int,readline().split()))
L = sorted(L)

# 2本固定すると、もう一本として選べるのは、2本の和より長いものだけ
# これを二分探索で数える

#print(L)
import bisect
ans = 0
for i in range(N - 1):
  for j in range(i + 1,N):
    limit = L[i] + L[j]
    ok = bisect.bisect_left(L, limit)
#    print("i",i,"j",j,"L[i]",L[i],"L[j]",L[j],"limit",limit,"ok",ok,"ok - j",ok - 1 - j)
    ans += ok - 1 - j
        
print(ans)