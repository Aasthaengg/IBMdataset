N = int(input())
S = input()

l = 0
for i in range(N):
    k = len(set(S[:i]) & set(S[i:]))
    if k > l:
        l = k
print(l)