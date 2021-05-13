import math
A,B,C = map(int,input().split())
k = [A,B,C]
k.sort()
k.reverse()
ans = 0
ans += k[0]-k[1]
now = k[2]
now += ans
if (k[0]-now)%2 == 0:
    ans += math.ceil((k[0]-now)/2)
    print(ans)
else:
    ans += math.ceil((k[0]-now)/2)
    ans += 1
    print(ans)
