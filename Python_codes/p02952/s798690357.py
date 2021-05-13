N = int(input())

keta = len(str(N))

if keta % 2 == 0:
     ans = 0
else:
     ans = N - 10 ** (keta-1) + 1

i = 1
while i < keta:
     ans += 10**i - 10**(i-1)
     i += 2


print(ans)