import math
N = float(input())
if N % 1000 == 0:
    print(0)
else:
    thousand_total =  math.ceil((N + 1) / 1000) * 1000
    print (int(thousand_total - N))
    
