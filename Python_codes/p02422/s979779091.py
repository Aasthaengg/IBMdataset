import sys
input = sys.stdin.readline

S = input().strip()
m = int(input())

for _ in range(m):
    ope = input().strip().split()
    a, b = int(ope[1]), int(ope[2])
    if ope[0] == "print":
        print(S[a:b+1])
    elif ope[0] == "reverse":
        S = S[:a] + S[a:b+1][::-1] + S[b+1:]
    elif ope[0] == "replace":
        S = S[:a] + ope[3] + S[b+1:]
