import itertools

A = range(int(input())+1)
B = range(int(input())+1)
C = range(int(input())+1)
X = int(input())

ans = 0
for coins in itertools.product(A, B, C):
    if (coins[0]*500+coins[1]*100+coins[2]*50) == X:
        ans += 1

print(ans)