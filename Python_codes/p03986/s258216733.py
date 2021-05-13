X = input()
n = len(X)
cnt = 0
S_check = 0

for i in range(n):
    if X[i] == 'S':
        S_check += 1

    if X[i] == 'T':
        if S_check > 0:
            S_check -= 1
        else:
            cnt += 1

print(cnt + S_check)