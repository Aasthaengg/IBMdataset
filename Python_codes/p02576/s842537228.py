n, x, t = map(int, input().split())
required_time = (n//x + 1)*t if n % x != 0 else (n//x)*t
print(required_time)