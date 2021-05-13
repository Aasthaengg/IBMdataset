A, B, C, D = map(int,input().split())

def answer(A: int, B: int, C: int, D: int) -> int:
    return max(A * B, C * D)

print(answer(A, B, C, D))
