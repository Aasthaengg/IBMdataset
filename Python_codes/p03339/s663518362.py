N = int(input())
S = input()
Wl = []
El = []
c = 0
for i in range(N):
    if S[i] == 'W':
        c += 1
    Wl.append(c)
c = 0
for i in range(N):
    if S[-(1 + i)] == 'E':
        c += 1
    El.append(c)
El.reverse()
Amin = min(El[1], Wl[N - 2])
for i in range(1, N - 2):
    A = Wl[i - 1] + El[i + 1]
    Amin = min(Amin, A)
print(Amin)