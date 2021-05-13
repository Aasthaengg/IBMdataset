A, B, C = map(int, input().split())
S = sorted([A,B,C])

if S[2] == S[0] + S[1]:
    print("Yes")
else:
    print("No")
