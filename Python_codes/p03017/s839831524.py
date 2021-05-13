N, A, B, C, D = map(int, input().split())
S = "#" + input() + "#"

# twoblock = S[A:].count("##")


def twoblock(start, end):
    return S[start : end + 1].count("##")


tripledot = S[B - 1 : D + 2].count("...")

if twoblock(A, C) or twoblock(B, D):
    print("No")
    exit()

if C > D:
    if tripledot == 0:
        print("No")
        exit()

print("Yes")

