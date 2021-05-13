S = input()
L = len(S) // 2
LS = list(S)

cnt = 0

for i in range(L):
    j = (i * -1) -1
    if LS[i] != LS[j]:
        cnt += 1

print(cnt)