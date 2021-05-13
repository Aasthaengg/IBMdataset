n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
ans = 0
hand = []

for i in range(len(t)):
    if t[i] == 'r':
        if i - k >= 0 and hand[i - k] == 'p':
            hand.append(' ')
            continue
        else:
            ans += p
            hand.append('p')
    elif t[i] == 's':
        if i - k >= 0 and hand[i - k] == 'r':
            hand.append(' ')
            continue
        else:
            ans += r
            hand.append('r')
    else:
        if i - k >= 0 and hand[i - k] == 's':
            hand.append(' ')
            continue
        else:
            hand.append('s')
            ans += s

print(ans)
