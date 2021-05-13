
def calculate(n):

    t = 1
    while True:
        s = ((1 + t) * t) // 2
        if s >= n:
            print(t)
            return t
        t = t + 1



calculate(int(input()))