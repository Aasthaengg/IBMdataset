# 入力
A, B, C = map(int, input().split())

# 出力
if -100 <= A and B and C <= 100:
    if A == B:
        print(C)
    elif B == C:
        print(A)
    elif A == C:
        print(B)