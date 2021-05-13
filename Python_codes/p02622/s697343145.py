S = input()
T = input()

Num = len(S)

S = list(S)
T = list(T)

change_num = 0

for i in range(Num):
    if S[i] is not T[i]:
        change_num += 1

print(change_num)