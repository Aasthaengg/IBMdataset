N = int(input())
a = [int(input()) for i in range(N)]

print("first" if any(map(lambda x: x % 2 == 1, a)) else "second")