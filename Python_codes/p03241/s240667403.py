import sys

def S(): return sys.stdin.readline().rstrip()

N,M = map(int,S().split())

# Mは、a1,…,aNの最大公約数の倍数になることに注意

divisor = []  # Mの約数

for i in range(1,int(M**.5)+1):
    if M % i == 0:
        divisor.append(i)
        if i != M//i:
            divisor.append(M//i)

ANS = []

for d in divisor:
    if d >= N:
        ANS.append(M//d)

print(max(ANS))