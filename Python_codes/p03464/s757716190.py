import math
k = int(input())
a = list(map(int, input().split()))
MAX = 2
MIN = 2
for i in a[::-1]:
    if MAX >= i:
        MAX = i * (MAX // i) + (i-1)
        MIN = i * (math.ceil(MIN / i)) 
        if MIN > MAX:
          print(-1)
          exit()
    else:
        print(-1)
        exit()
print(MIN,MAX)
