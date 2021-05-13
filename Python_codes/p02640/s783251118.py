X, Y = map(int, input().split())

def f():
    for turu in range(X + 1):
        if 2 * turu + 4 * (X - turu) == Y:
            return "Yes"
    return "No"

print(f())