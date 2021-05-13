mod = 10**9+7
N = int(input())
S1 = input()
S2 = input()

ans = 1
for i in range(N):
    if i == 0:
        if S1[i]==S2[i]:
            c = 3
        else:
            c = 6
    else:
        if S1[i-1]==S1[i]:
            c = 1
        else:
            if S1[i-1]==S2[i-1]:
                c = 2
            elif S1[i]==S2[i]:
                c = 1
            else:
                c = 3
    ans *= c
    ans %= mod
print(ans)