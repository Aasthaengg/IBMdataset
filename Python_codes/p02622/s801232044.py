S = input()
T = input()

cnt = 0

for i in range(len(S)):
    cnt += (S[i] != T[i])

print(cnt)