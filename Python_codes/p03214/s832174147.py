# A - Thumbnail

from statistics import mean

N = int(input())
a = list(map(int, input().split()))
a2 = [abs(x - mean(a)) for x in a]

print(a2.index(min(a2)))