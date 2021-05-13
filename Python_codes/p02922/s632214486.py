import math
a, b = map(int, input().split())
ans=1
if b==1:
    print(0)
elif b<=a:
    print(ans)
else:
    print(math.ceil((b-a)/(a-1))+1)
