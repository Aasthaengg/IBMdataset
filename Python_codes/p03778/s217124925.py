def resolve():
    w, a, b = map(int, input().split())
    print(min(abs(b-a-w), abs(a-b-w)) if b-a > w or a-b >w else "0")
resolve()