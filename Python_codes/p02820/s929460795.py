N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
keys = [i for i in range(N)]
hands = {key: 0 for key in keys}  # n回目の手を記録

for i in range(N):
    if i < K:
        if T[i] == 'r':
            hands[i] = P
        elif T[i] == 's':
            hands[i] = R
        else:
            hands[i] = S
    elif i >= K:
        if T[i] == T[i-K] == 'r':
            if hands[i-K] == 0:
                hands[i] = P
        elif T[i] == T[i-K] == 's':
            if hands[i-K] == 0:
                hands[i] = R
        elif T[i] == T[i-K] == 'p':
            if hands[i-K] == 0:
                hands[i] = S
        else:
            if T[i] == 'r':
                hands[i] = P
            elif T[i] == 's':
                hands[i] = R
            else:
                hands[i] = S

total = sum(hands.values())
print(total)
