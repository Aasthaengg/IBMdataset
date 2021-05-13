N,X = map(int,input().split())
m = []
for i in range(N):
    m.append(int(input()))
min_ = sorted(m)[0]
counter = 0
for j in range(N):
    X = X - m[j]
    counter += 1
counter += X // min_
print(counter)