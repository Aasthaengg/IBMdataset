import math
A, B = map(int,input().rstrip().split())
ans = math.ceil((B-1)/(A-1))
print(ans)