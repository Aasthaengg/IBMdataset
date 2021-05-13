S = input()
N = len(S)
a = 0
ans = 0
f = 0
for i in range(N-1):
    if S[i] == 'A':
        a += 1
    elif S[i] == 'B':
        if S[i+1] == 'C':
            ans += a
            f = 1
        else:
            a = 0
    else:
        if f != 1:
            a = 0
        else:
            f = 0
print(ans)