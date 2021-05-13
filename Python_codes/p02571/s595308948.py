S = input()
s = len(S)
T = input()
t = len(T)

cnt = t
for i in range(s-t+1):
    dif = 0
    for j in range(t):
        if S[i+j] != T[j]:
            dif += 1
    if cnt > dif:
        cnt = dif
print(cnt)
