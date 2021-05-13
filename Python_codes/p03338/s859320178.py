N = int(input())
S = input()

lst = [None]*(N-1)
for i in range(N-1):
    X = S[:i]
    Y = S[i:]
    lst[i] = len(set(X) & set(Y))
print(max(lst))