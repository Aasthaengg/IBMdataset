N=int(input())
ABC=[list(input()) for _ in range(3)]

R=[len(set(x))-1 for x in zip(*ABC)]

print(sum(R))
