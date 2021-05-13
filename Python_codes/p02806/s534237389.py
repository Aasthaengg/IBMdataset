N = int(input())
ST = [input().split() for _ in range(N)]
X = input()

S,T = zip(*ST)

i = S.index(X)
print(sum(map(int,T[i+1:])))