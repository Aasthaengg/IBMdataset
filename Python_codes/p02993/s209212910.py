flg = True
S = input()

for i in range(1, 4):
    if S[i] == S[i - 1]:
        flg = False

print("Good" if flg else "Bad")