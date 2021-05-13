S = input()

def solve(S):
    a = 0
    return S.count("+") - S.count("-")

print(solve(S))