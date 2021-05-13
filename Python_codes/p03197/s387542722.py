N = int(input())
a = [int(input()) for _ in range(N)]
for e in a:
    if e%2 == 1:
        print("first")
        exit(0)
print("second")
