a, b, c = map(int, input().split())
print(max((a*10+b+c), (b*10+c+a), (c*10+a+b)))
