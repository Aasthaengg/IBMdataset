def check(s):
    for i in range(len(s) - 1):
        if s[i] == '#' and s[i + 1] == '#':
            return False
    return True


def checksp(s):
    for i in range(len(s) - 2):
        if s[i] == '.' and s[i + 1] == '.' and s[i + 2] == '.':
            return True
    return False


N, A, B, C, D = map(int, input().split(" "))
S = input()
A -= 1; B -= 1; C -= 1; D -= 1;

if C < D:
    if check(S[A:C+1]) and check(S[B:D+1]):
        print('Yes')
    else:
        print('No')
else:
    if checksp(S[B-1:D+2]) and check(S[B:D+1]) and check(S[A:C+1]):
        print('Yes')
    else:
        print('No')