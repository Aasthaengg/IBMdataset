# D - We Love ABC

S = list(input())
MOD = 10**9 + 7

n_possible = 1 # その場所以前の文字列としてあり得るパターン
A = 0 # その場所以前の文字列におけるA数
B = 0
C = 0

for s in S:
    if s == "A":
        A += n_possible
    elif s == "B":
        B += A
    elif s == "C":
        C += B
    else:
        # X = 3*X + Y
        # この場所の？を (AorABorABCの一部に含めない場合) + (AorABorABCの一部に含める場合)
        C = 3*C + B
        B = 3*B + A
        A = 3*A + n_possible
        n_possible *= 3
    n_possible %= MOD
    A %= MOD
    B %= MOD
    C %= MOD
        
print(C)