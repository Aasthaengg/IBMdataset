n, h, w = list(map(int, input(" ").split()))
lst = [list(map(int, input().split(" "))) for i in range(n)]

result = 0
for a, b in lst:
    if (a >= h and b >= w):
        result += 1

print(result)
