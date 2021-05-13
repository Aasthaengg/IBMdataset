N = int(input())
S = input()
MAX = 0
for T in range(0,N+1):
    X = S[:T]
    Y = S[T:]
    Com = len(set(X)&set(Y))
    if Com>MAX:
        MAX = Com
print(MAX)