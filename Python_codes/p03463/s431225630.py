N, A, B = map(int, input().split())
print("Alice" if not (A-B)%2 else "Borys")