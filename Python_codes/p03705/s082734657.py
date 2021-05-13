n, a, b = map(int, input().split())
if (n == 1 and a != b) or a > b:
    print(0)
else:
    print((n-1)*b+a-((n-1)*a+b)+1)
