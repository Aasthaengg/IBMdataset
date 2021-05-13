N = int(input())
S = input().strip()
cmax = 0
for i in range(1,N-1):
    X = set(list(S[:i]))
    Y = set(list(S[i:]))
    Z = X&Y
    cmax = max(cmax,len(Z))
print(cmax)