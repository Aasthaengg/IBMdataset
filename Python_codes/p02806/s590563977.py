N = int(input())
S = []
T = []

for i in range(N):
    s, t = input().split()
    t = int(t)
    S.append(s)
    T.append(t)

X = input()
num = None

for i in range(N):
    if X == S[i]:
        num = i + 1
        break

total = sum(T[num:N])

print(total)