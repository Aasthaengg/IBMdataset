
N, K = map(int, input().split())
S = input()

cnt = S.count("RL")
edge = int(S[0] == "L") + int(S[-1] == "R")

print(min(N - 1, N - 2 * cnt - edge + K * 2))
