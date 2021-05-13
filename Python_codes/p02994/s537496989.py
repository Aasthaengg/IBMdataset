n, l = map(int, input().split())
x = [l+i for i in range(n)]
x = sorted(x, key=lambda x: abs(x))
print(sum(x[1:]))