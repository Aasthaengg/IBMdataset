N = int(input())
A = sum([int(input()) % 2 for _ in range(N)])

print("first" if A else "second")