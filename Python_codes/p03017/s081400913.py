n, a, b, c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
S = input()

if c < d:
    while b < d:
        if S[b+1] == '.':
            b += 1
        elif b+2 <= d and S[b+2] == '.':
            b += 2
        else:
            print('No')
            exit()
    while a < c:
        if S[a+1] == '.':
            a += 1
        elif a+2 <= c and S[a+2] == '.':
            a += 2
        else:
            print('No')
            exit()
else:
    while a < c:
        if a+1 == b and S[a+2] == '.' :
            a += 2
        elif a+1 == b and a+3 <= d and S[a+3] == '.':
            b += 2
            a += 1
        elif S[a+1] == '.' and a+1 != b:
            a += 1
        elif a+2 == b and a+3 <= d and S[a+3] == '.':
            a += 2
            b += 1
        elif a+2 == b and a+4 <= d and S[a+4] == '.':
            a += 2
            b += 2
        elif S[a+2] == '.' and a+2 != b:
            a += 2
        else:
            print('No')
            exit()
    while b < d:
        if S[b+1] == '.':
            b += 1
        elif b+2 <= d and S[b+2] == '.':
            b += 2
        else:
            print('No')
            exit()
print('Yes')