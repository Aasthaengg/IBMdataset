def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


X, Y = list(map(int, input().split()))
Turtle = (Y - 2*X ) / 2
Crane = X - Turtle
if Turtle >= 0 and Crane >= 0 and is_integer(Turtle) and is_integer(Crane):
    print("Yes")
else:
    print("No")