N = int(input())
S = input()

countE = [0]*(N+1)
countW = [0]*(N+1)

for i in range(N):
    countW[i + 1] = countW[i]
    if S[i] == 'W':
        countW[i+1] += 1

for i in range(1, N):
    countE[N-i-1] = countE[N-i]
    if S[N-i] == 'E':
        countE[N-i - 1] += 1

minx = N+1
for i in range(N):
    newv = countW[i] + countE[i]
    if minx > newv:
        minx = newv

print(minx)
