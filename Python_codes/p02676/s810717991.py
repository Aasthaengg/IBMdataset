# Triple Dots
K = int(input())
S = input()
ans = S[:K] + ['...', ''][len(S) <= K]
print(ans)
