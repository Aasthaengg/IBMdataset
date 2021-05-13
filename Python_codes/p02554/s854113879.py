N = int(input())

Q = 10 ** 9 + 7

a10 = 1
a9 = 1
a8 = 1

for _ in range(N):
    a10 *= 10 
    a9 *= 9 
    a8 *= 8
      
    a10 %= Q
    a9 %= Q
    a8 %= Q

ans = (a10 - (2 * a9 - a8)) % Q

print(ans)