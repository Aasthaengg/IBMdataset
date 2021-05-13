lim = 1000000007
result = 1
n = int(input())

for q in range(n):
    result = result % lim
    result *= q + 1
print(result % lim)