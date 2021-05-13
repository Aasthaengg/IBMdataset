def solve(a, b):
    mod = 1
    while mod != 0:
        mod = b%a
        b = a
        a = mod
    return b

N = int(input())
A = list(map(int, input().split()))

minA = min(A)
B = [a%minA for a in A]
print(solve(minA, max(B)))