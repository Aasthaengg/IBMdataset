N,L = map(int, input().split())

Ls = [L + i for i in range(N)]

print(sum(Ls)-min(Ls, key=abs))