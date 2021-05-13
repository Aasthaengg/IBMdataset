S = input()
T = input()
lS = len(S)
lT = len(T)
C = []
for i in range(lS-lT+1):
    count = 0
    for j in range(lT):
        if S[i+j]!=T[j]:
            count += 1
    C.append(count)
print(min(C))