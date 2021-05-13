debug = False

if debug:import time
if debug:start = time.time()

n = int(input())
R = [0]*n
R_min = 10**9

for i in range(n):
    R[i] = int(input())

maximum_profit = -10**9
for i in range(1, n):
    R_min = R[i-1] if R[i-1] < R_min else R_min
    profit = R[i] - R_min
    maximum_profit = profit if profit > maximum_profit else maximum_profit
print(maximum_profit)

if debug:print(time.time() - start)