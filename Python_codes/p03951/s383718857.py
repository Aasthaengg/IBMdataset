N = int(input())
S = input()
T = input()
for i in range(N + 1):
    if S[i:] == T[: N - i]:
        print(N + i)
        break
