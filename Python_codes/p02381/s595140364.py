import math
while(True):
    n = int(input())
    if(n == 0): break
    s = list(map(int, input().split()))
    print(math.sqrt(sum([(x - sum(s)/n)**2 for x in s]) / n))