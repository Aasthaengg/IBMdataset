n=int(input())
from bisect import bisect_left as bl,bisect_right as br
a,b,c=[list(map(int,input().split())) for i in range(3)]
a.sort()
c.sort()
print(sum(bl(a,i)*(n-br(c,i))for i in b))