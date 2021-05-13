N, i = map(int, input().split())
train = []
for j in range(1,N+1):
    train.append(j)
train.sort(reverse=True)

print(train[i-1])