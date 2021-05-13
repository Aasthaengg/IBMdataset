from statistics import median
N = int(input())
As = list(map(int,input().split()))
calcA = sorted([As[i]-(i+1) for i in range(len(As))])
med = median(calcA)
print(int(sum([abs(As[i]-(med+i+1)) for i in range(len(As))])))