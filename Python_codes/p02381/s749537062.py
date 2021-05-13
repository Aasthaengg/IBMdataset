import math
while True:
    n = int(input())
    if n == 0:
        break
    inp = list(map(float,input().split()))
    m = sum(inp)/len(inp)
    stdev = math.sqrt(sum([(s-m)**2 for s in inp])/len(inp))
    print(stdev)