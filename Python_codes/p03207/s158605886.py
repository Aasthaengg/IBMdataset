N = int(input())
P = sorted(int(input()) for n in range(N))
print(sum(P[:-1])+P[-1]//2)