import math
a = int(input())
b = int(input())
c = list(map(int,input().split()))
ans = 0
for i in range(a):
    tmp = min(c[i],b-c[i])
    ans+=tmp
print(ans*2)