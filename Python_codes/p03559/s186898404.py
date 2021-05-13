n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a = sorted(a)
b = sorted(b)
c = sorted(c)
count = 0
import bisect
for i in range(n):
    A = bisect.bisect_right(a,b[i]-1)
    C = bisect.bisect_left(c,b[i]+1)
    count += A*(n-C)
print(count)