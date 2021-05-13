S = str(input())
i = 0
error = 0

while i < len(S) and error == 0:

    if i + 5 > len(S):
        error = -1
        break

    if S[i: i + 5] == 'dream':
        i += 5
        if i + 2 <= len(S):
            if S[i: i + 2] == 'er':
                if (i + 2) == len(S):
                    i += 2
                elif S[i + 2] != 'a':
                    i += 2
    elif S[i: i + 5] == 'erase':
        i += 5
        if i + 1 <= len(S):
            if S[i] == 'r':
                if (i + 1) == len(S):
                    i += 1
                elif S[i + 1] != 'a':
                    i += 1
    else:
        error = -1
        break

if error == 0:
    print('YES')
else:
    print('NO')