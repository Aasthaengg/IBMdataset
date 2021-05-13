N, A, B = map(int, input().split())
sp = max(A, B) - min(A, B) - 1
if sp % 2 == 1:
    print("Alice")
else:
    print("Borys")