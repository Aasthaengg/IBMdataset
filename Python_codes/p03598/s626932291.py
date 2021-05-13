import sys
N = int(input())
K = int(input())
coordinate = list(map(int,input().split()))
if N < 0 or N > 100 or K < 0 or K > 100:
    sys.exit()

sum_min = 0
for x in coordinate:
    if x < 0 or x >= K:
        sys.exit()
    if x * 2 <= (K - x) * 2:
        sum_min += x * 2
    else:
        sum_min += (K - x) * 2
print(sum_min)