def sign(n):
    if n == 0:
        return 0
    return n // abs(n)

a, b = map(int, input().split())

print("a", end = " ")
ans = ["<", "==", ">"][1 + sign(a - b)]
print(ans, end = " ")

print("b")
