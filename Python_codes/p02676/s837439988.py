K = int(input())
S = input()
ans = S if len(S) <= K else S[:K] + "..."
print(ans)