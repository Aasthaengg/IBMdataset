import sys

a, b, c = map(int, sys.stdin.readline().split())

c_prime = []
for i in range(1, c+1):
    if(c % i == 0):
        c_prime.append(i)

ans = 0
for i in range(a, b+1):
    if(i in c_prime):
        ans += 1

print(ans)