N = int(input())
s = ""
S = []
for i in range(N):
    s = input()
    S.append(s)
M = int(input())
t = ""
T = []
for i in range(M):
    t = input()
    T.append(t)
#青いカードSi * N 赤いカードTi * M
S = sorted(S)
T = sorted(T)
W = []
c = -1
num = []
for i in range(N):
    if not(S[i] in W):
        W.append(S[i])
        num.append(0)
        c += 1
        for j in range(i,N):
            if W[c] == S[j]:
                num[c] += 1
        for j in range(M):
            if W[c] == T[j]:
                num[c] -= 1
num.append(0)
print(max(num))
