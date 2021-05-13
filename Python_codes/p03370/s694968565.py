N, X = map(int, input().split())
m = sorted([int(input()) for _ in range(N)], reverse=False)
sum = 0
for i in range(N):
    sum += m[i]
    if sum > X:
        print(i)
        break
    elif i == N - 1:
        print(i + 1 + (X - sum) // m[0])