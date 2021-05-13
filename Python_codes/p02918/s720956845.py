N, K = map(int, input().split(' '))
S = input()
happy = sum([1 for i in range(N - 1) if S[i] == S[i + 1]])
print(min(N - 1, happy + 2 * K))