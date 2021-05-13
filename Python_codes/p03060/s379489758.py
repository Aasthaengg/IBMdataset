import sys
N = int(input())
array_value = list(map(int,input().split()))
array_cost = list(map(int,input().split()))

if not ( 1 <= N <= 20 ): sys.exit()
for I in array_value:
    if not ( 1 <= I <= 50 ): sys.exit()
for J in array_cost:
    if not ( 1 <= J <= 50 ): sys.exit()

value_check = 0
for K in range(len(array_value)):
    value = array_value[K] - array_cost[K]
    value_check += value if value >= 1 else 0

print(value_check)