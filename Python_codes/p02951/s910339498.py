# 136_a
A, B, C = map(int, input().split())
if (A >= B) & (1 <= A & A <= 20) & (1 <= B & B <= 20) & (1 <= C & C <= 20):
    case1_rest = A - B
    if case1_rest < C:
        case2 = C - case1_rest
    elif case1_rest >= C:
        case2 = 0
    print(case2)