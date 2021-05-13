N = int(input())
D = list(map(int, [input() for _ in range(N)]))

D = list(set(D))
print(len(D))