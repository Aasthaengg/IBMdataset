# B - Christmas Eve Eve
N = int(input())
P = [int(input()) for _ in range(N)]
P = sorted(P)
P[-1] = P[-1]//2
print(sum(P))
