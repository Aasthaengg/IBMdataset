N, M = map(int, input().split())
order = [i for i in range(2, N+1)]
reverse = order[::-1]
d = 0
for i in range(M):
    if N%4 == 0 and reverse[i] - order[i] == N//2:
        d = 1
    if N%2 == 0 and i == (N//2-1) //2:
        d = 1
    print(order[i+d], reverse[i])