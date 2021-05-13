N = int(input())
import math
if int(math.floor((math.ceil(N/1.08) * 1.08)))==N:
    print(int(math.ceil(N/1.08)))
else:
     print(":(")  