n = int(input())
d = sorted(list(map(int,input().split())))
#print(d)
cnt = 0
import bisect
for k in range(1,d[n-1]+1):
    if bisect.bisect_left(d,k) == n//2:
        cnt += 1
        #print(bisect.bisect_left(d,k))
        #print(k)
print(cnt)