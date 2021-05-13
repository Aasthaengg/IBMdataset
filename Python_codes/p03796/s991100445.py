N = int(input())
P = 1
D = 10**9 + 7

for n in range(1, N+1):
    P = (P * n) % D

print(P%D)