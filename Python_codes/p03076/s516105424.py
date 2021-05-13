# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
import math
from operator import itemgetter
input = sys.stdin.readline

list_time = [int(input()) for i in range(5)]
list_CeilMati = [[0, 0] for i in range(5)]

temp = 0.0
for i in range(5):
    temp = list_time[i]/10
    list_CeilMati[i][0] = math.ceil(temp) * 10
    list_CeilMati[i][1] = list_CeilMati[i][0] - list_time[i]

# print(list_CeilMati)
list_CeilMati.sort(key=lambda x: x[1])
# print(list_CeilMati)

ans = 0
for i in range(5):
    ans += list_CeilMati[i][0]
ans -= list_CeilMati[5-1][1]

print(ans)
