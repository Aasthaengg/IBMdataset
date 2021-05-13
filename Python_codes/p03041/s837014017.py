N, K = map(int, input().split())
S = input()
[print(S[i].lower(), end='') if i == K-1 else print(S[i], end='') for i in range(len(S))]