A, B = list(map(int, input().split()))

is_divisor = B % A == 0
answer = A + B if is_divisor else B - A

print(answer)