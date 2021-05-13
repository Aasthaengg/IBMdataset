S = input()
if len(S) != 26:
    for i in range(26):
        if chr(ord('a') + i) not in S:
            print(S + chr(ord('a') + i))
            break
elif S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
else:
    can = []
    for i in range(26):
        if len(can) >= 1 and can[-1] > ord(S[-1-i]):
            for s in can:
                if s > ord(S[-1-i]):
                    print(S[:-1-i] + chr(s))
                    exit(0)
        can.append(ord(S[-1-i]))
