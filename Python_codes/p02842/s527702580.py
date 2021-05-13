import math
N = int(input())
ans = math.ceil(100*N/108)
if math.floor(ans*1.08) == N:
    print(ans)
else:
    print(":(")
