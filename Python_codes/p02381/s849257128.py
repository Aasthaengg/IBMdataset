import math
import statistics
while 1:
    n = int(input())
    if n == 0:  break
    data = list(map(int, input().split()))
    #print(data)
    print(statistics.pstdev(data))
