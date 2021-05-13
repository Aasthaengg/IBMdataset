N, C,K = map(int, input().split())

T = []
for _ in range(N):
    T.append(int(input()))

T = sorted(T)

Standard = T[0] + K
count = 1


ans = 0
for i in range(1,N):
    if (count == C) or (Standard < T[i]):
        ans = ans + 1
        count = 1 
        Standard = T[i] + K
    else:
        count = count + 1

print(ans+1)
