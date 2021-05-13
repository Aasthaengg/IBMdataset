def solve():
    S = input()

    s = [0 for _ in range(len(S))]
    for i, si in enumerate(S):
        if si == 'R':
            t = S[i:].index('L')
            if t % 2 == 0:
                s[i+t] += 1
            else:
                s[i+t-1] += 1
        else:
            t = S[:i].rfind('R')
            if (i - t) % 2 == 0:
                s[t] += 1
            else:
                s[t+1] += 1
                
    return s

print(*solve())