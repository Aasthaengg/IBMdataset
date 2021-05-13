N = int(input())
S = input()

s = set()
L = [[set() for i in range(2)] for j in range(N+1)]

ans = set()

for i in range(N):
    L[i+1][0].add(S[i])
    for k in L[i][0]:
        L[i+1][0].add(k)
        L[i+1][1].add(k + S[i])
    for k in L[i][1]:
        L[i+1][1].add(k)
        ans.add(k + S[i])

print(len(ans))