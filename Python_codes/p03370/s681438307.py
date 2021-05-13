N,X = map(int,input().split())
m = [int(input()) for _ in range(N)]
count = 0

X = X -sum(m)
count += len(m)
count += (X // min(m))

print(count)


