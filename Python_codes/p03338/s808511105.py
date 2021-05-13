N = int(input())
S = input()

ans = 0

for i in range(N-1):
    set1 = set(S[:i+1])
    set2 = set(S[i+1:])
    
    ans = max(ans, len(set1&set2))
    
print(ans)