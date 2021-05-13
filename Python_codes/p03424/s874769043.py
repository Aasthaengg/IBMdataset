def resolve():
    N = int(input())
    hina = list(input().split())
    print("Three" if len(set(hina)) == 3 else "Four")
resolve()