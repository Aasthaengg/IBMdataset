x = int(input())

from itertools import accumulate

pos = 0
ans = 0
while pos < x:
    ans+=1
    pos+=ans

print(ans)