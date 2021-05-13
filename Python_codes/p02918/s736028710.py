N, K = map(int, input().split())
S = input()
happy = 0
for n in range(N):
    if S[n] == "L" and n > 0 and S[n - 1] == "L":
        happy += 1
    elif S[n] == "R" and n < N - 1 and S[n + 1] == "R":
        happy += 1
print(min(happy + 2 * K, N - 1))
