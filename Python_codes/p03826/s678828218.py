A,B,C,D = map(int, input().split())
S_AB = A * B
S_CD = C * D
if S_AB > S_CD:
    print(S_AB)
else:
    print(S_CD)