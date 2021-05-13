n, x, t = map(int, input().split(" "))
takoyaki = (n // x) * t

if n % x != 0:
    takoyaki += t

print(takoyaki)
