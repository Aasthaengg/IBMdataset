n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]


a.sort()
c.sort()

from bisect import bisect_left,bisect_right
cnt = 0
for i in b:
    cnt += bisect_left(a,i)*(n-bisect_right(c,i))

print(cnt)