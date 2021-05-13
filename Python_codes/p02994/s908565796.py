N, L = map(int,input().split())
T = []
A = 0
for i in range(N):
    T.append(L + i)

if T[0] <= 0 and T[-1] >= 0:
    A = sum(T)

elif T[-1] < 0:
    A = sum(T[:-1])

else:
    A = sum(T[1:])

print(A)