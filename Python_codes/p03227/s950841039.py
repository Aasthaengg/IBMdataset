S = input()
N = len(S)
ans = S if N == 2 else S[::-1]
print(ans)