S = input()
N = len(S)

hand = {'g': 0, 'p': 0}
ans = 0
for i in range(N):
    if S[i] == 'g':
        if hand['g'] > hand['p']:
            hand['p'] += 1
            ans += 1
        else:
            hand['g'] += 1
    else:
        if hand['g'] > hand['p']:
            hand['p'] += 1
        else:
            hand['g'] += 1
            ans -= 1

print(ans)