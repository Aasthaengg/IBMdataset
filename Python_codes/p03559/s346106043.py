# 2019/08/07
# Bのソートは不要！！

from bisect import bisect_left,bisect_right

n=int(input())
a=sorted(list(map(int,input().split())))
b=list(map(int,input().split()))
c=sorted(list(map(int,input().split())))
ans=0

for i in range(n):
    bc=n-bisect_right(c,b[i])
    ba=bisect_left(a,b[i])
    ans+=bc*ba    

print(ans)
