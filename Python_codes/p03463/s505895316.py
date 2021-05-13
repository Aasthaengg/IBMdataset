def solve(n, a, b):
    for t in range(n*2):
        if t % 2 == 0:
            if a < b + 1:
                a += 1
            elif a == b + 1:
                a += 1
            elif a == b - 1:
                a -= 1
            elif a > b - 1:
                a -= 1
            else:
                return "Borys"
        else:
            if b < a + 1:
                b += 1
            elif b == a + 1:
                b += 1
            elif b == a - 1:
                b -= 1
            elif b > a - 1:
                b -= 1
            else:
                return "Alice"
        if a == b:
            return "Borys" if t % 2 == 0 else "Alice"
        if (a <= 0) or (n < a):
            return "Borys"
        elif (b <= 0) or (n < b):
            return "Alice"
    return "Draw"

n, a, b = map(int, input().split())
print(solve(n, a, b))