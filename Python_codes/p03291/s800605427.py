MOD = 10**9 +7
S = input().rstrip()
A = 0
B = 0
C = 0
X = 1
for s in S:
    if s=="?":
        C=B + C*3
        B=A + B*3
        A=X + A*3
        X *= 3
    else:
        if s=="A":
            A+=X
        if s=="B":
            B+=A
        if s =="C":
            C+=B
    X %= MOD
    A %= MOD
    B %= MOD
    C %= MOD
print(C)