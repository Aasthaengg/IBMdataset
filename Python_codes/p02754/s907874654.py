# A: blue, B: red
N, A, B = map(int, input().split())
# N, A, B = 8,0,4
#print(N)

q, mod = divmod(N, A+B)
if mod < A:
    extra = mod
else:
    extra = A
result = q * A + extra

print(result)