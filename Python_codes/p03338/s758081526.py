N = int(input())
S = input()

ans = 0

for k in range(1, N):
    ans = max(ans, len(set(S[:k])&set(S[k:])))
    
print(ans)