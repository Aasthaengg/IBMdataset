X = input()

S_cnt = 0
T_cnt = 0
for i in range(len(X)):
    if X[i] == 'S':
        S_cnt += 1
    else:
        if S_cnt > 0:
            S_cnt -= 1
        else:
            T_cnt += 1

print(S_cnt+T_cnt)
