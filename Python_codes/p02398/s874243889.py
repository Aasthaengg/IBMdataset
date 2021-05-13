a, b, c = map(int, input().split())
print(sum(not (c % i) for i in range(a, b + 1)))