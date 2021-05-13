S = input()
mojisu = len(S)
ans = 0
for i in range(mojisu//2):
    ans += S[i] != S[mojisu-i-1]
print(ans)
