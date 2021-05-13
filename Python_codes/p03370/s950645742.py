N,X = map(int,input().split())
m = [input() for i in range(N)]

m = list(map(int, m))

X = X - sum(m)

min_m = min(m)

C = N + X // min_m

print(C)