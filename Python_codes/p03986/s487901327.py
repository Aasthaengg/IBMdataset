X = input()
n = len(X)
S_waitng_for_T = 0
ans = n
for i in range(n):
    if X[i] == 'S':
        S_waitng_for_T += 1
    else:
        if S_waitng_for_T > 0:
            S_waitng_for_T -= 1
            ans -= 2
print(ans)
