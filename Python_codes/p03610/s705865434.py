S = list(input())
N = len(S)
T = []
for i in range(N):
    if i%2==0:
        T.append(S[i])
print("".join(T))
