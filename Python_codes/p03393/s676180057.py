from string import ascii_lowercase
S = input()
if S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()
if len(S) < 26:
    for a in ascii_lowercase:
        if a not in S:
            print(S + a)
            exit()
can = []
for i in range(25, 0, -1):
    can.append(S[i])
    if S[i - 1] < S[i]:
        for c in sorted(can):
            if S[i - 1] < c:
                print(S[:i - 1] + c)
                exit()
