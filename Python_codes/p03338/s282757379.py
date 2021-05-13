N = int(input())
S = input().rstrip()
res = 0
for i in range(N):
    res = max(len(set(S[i:]) & set(S[:i])), res)
print(res)