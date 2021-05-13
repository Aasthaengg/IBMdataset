def resolve():
    A, B = map(int, input().split())
    print("Impossible" if A%3 != 0 and B%3 != 0 and (A+B)%3 != 0 else "Possible")
resolve()