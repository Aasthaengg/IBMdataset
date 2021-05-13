S = input()
N = len(S)
r = 0
l = 0
ans = 0
while l+r < N:
    if S[l] == S[N-1 - r]:
        l += 1
        r += 1
    else:
        if S[l] == 'x':
            l += 1
            ans += 1
        elif S[N-1 - r] == 'x':
            r += 1
            ans += 1
        else:
            print(-1)
            exit()

print(ans)