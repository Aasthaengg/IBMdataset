a, b, c = sorted(list(map(int, input().split())))
k = int(input())
print(a + b + c * (2 ** k))