N = int(input())
print("first" if sum([int(input()) % 2 for _ in range(N)]) > 0 else "second")