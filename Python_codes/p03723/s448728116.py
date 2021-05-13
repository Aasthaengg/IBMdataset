def calculate(A, B, C):
    for i in range(1000):
        if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
            return i
        else:
            _A = (B + C) // 2
            _B = (A + C) // 2
            _C = (A + B) // 2
            A, B, C = _A, _B, _C
    return -1

A, B, C = map(int, input().split())
print(calculate(A, B, C))