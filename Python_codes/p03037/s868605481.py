n, m = map(int, input().split())
a = [ list(map(int, input().split())) for i in range(m) ]
print(max(min(a, key=lambda x: x[1])[1] - max(a, key=lambda x: x[0])[0] + 1, 0))