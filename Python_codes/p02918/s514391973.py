N, K = map(int, input().split())
S = input()

x = S.count("RL")
y = int(S[0] == "L") + int(S[-1] == "R")
print(min(N - 1, N - 2 * x - y + 2 * K))
