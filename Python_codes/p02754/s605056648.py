N, A, B = map(int, input().split())

result = (N // (A+B)) * A

if N % (A+B) <= A:
    result += N % (A+B)
else:
    result += A

print(result)