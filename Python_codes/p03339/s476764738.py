N = int(input())
S = input()

ans = []
t = [0]*(N+1)

for i in range(N): #i人までにいる東向きの人
    if S[i] == "E":
        t[i+1] = t[i] + 1
    else:
        t[i+1] = t[i]

for j in range(N):
    ans.append(j + t[N] - t[j]  - t[j+1])

print(min(ans))