a, b = map(int, input().split())

for i in range(max(a, b)):
    print(str(min(a, b)), end="")
