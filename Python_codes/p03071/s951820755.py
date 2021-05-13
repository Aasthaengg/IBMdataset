a, b = map(int, input().split())
# = list(map(int, input().split()))
# = [int(input()) for _ in range()]
if max(a, b) - min(a, b) > 0:
    print(max(a, b) * 2 - 1)
else:
    print(max(a, b) * 2)
