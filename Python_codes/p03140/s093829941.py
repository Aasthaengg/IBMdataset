N = int(input())
A = input()
B = input()
C = input()

res = 0
for a, b, c in zip(A, B, C):
    if a != b and b != c and c != a:
        res += 2
    elif a == b == c:
        pass
    else:
        res += 1

print(res)
