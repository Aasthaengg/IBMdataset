MOD = 10**9 + 7
n = int(input())
start = 1
for i in range(2, n+1):
    start *= i
    start %= MOD
print(start)