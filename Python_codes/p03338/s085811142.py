N = int(input())
S = input()

ans = []

for i in range(1, N):
    l = set(S[:i])
    r = set(S[i:])
    ans.append(len(l & r))
print(max(ans))