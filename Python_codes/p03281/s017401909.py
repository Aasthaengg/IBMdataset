import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

n = int(input())

def num_divisors_table(n):
    table = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1
    
    return table

table = num_divisors_table(n)
ans = 0
for i in range(1, n + 1, 2):
    if table[i] == 8:
        ans += 1
print(ans)