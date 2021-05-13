def resolve():
    A, B, X = list(map(int, input().split(" ")))
    if X >= A:
        print("YES" if B >= X - A else "NO")
    else:
        print("NO")

if '__main__' == __name__:
    resolve()