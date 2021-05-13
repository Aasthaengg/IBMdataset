n = int(input())
S = []
T = []

for i in range(n):
    s, t = map(str, input().split())
    t = int(t)
    S.append(s)
    T.append(t)

x = str(input())

for i in range(n):
    if S[i] == x:
        j = i

if j == n-1:
    print(0)
else:
    print(sum(T[j+1:]))
