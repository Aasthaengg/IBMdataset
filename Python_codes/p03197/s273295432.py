n = int(input())
l = [int(input()) for _ in range(n)]
print("second" if all(a % 2 == 0 for a in l) else "first")