N, A, B = [int(n) for n in input().split(" ")]

s = N // (A + B)
t = N % (A + B)

a = A
if t < A:
    a = t

print(s * A + a)