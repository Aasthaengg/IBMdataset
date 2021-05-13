S = []
T = []

N = int(input())
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

X = input()
x = S.index(X)

print(sum(T[x:]) - T[x])
