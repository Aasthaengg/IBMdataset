N, A, B, C, D = map(int, input().split())
S = input()
S = "#" + S + "#"

# A -= 1
# B -= 1
# C -= 1
# D -= 1

def can_reach(start, end):
    for i in range(start, end + 1):
        if S[i] == '#' and S[i + 1] == '#':
            return False
    return True


if not can_reach(A, C) or not can_reach(B, D):
    print("No")
    exit()

if C > D:
    cover = False
    for i in range(B, D + 1):
        if S[i - 1] == '.' and S[i] == '.' and S[i + 1] == '.':
            cover = True
    if not cover:
        print("No")
        exit()


print("Yes")