from math import gcd
n = int(input())

time = list(int(input()) for _ in range(n))

ans = time[0]

for i in range(1,n):
    ans = (ans * time[i]) // gcd(ans, time[i])

print(int(ans))