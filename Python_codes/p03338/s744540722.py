N = int(input())
S = str(input())

lst = [0]*N

for i in range(N):
    X = list(set(list(S[0:i])))
    Y = list(set(list(S[i:N])))
    ans = 0
    for j in range(len(X)):
        if X[j] in Y:
            ans += 1
    lst[i] = ans

print(max(lst))
