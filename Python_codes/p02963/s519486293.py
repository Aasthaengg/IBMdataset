
S = int(input())
a, b = divmod(S, 10**9)
if b > 0:
    b = 10**9-b
    a += 1
print(0, 0, 10**9, 1, b, a)
