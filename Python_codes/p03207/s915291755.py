N = int(input())
P = sorted(map(int,(list((input() for _ in range(N))))),reverse = True)
P[0] = P[0]//2
print(sum(P))