a,b = map(int, raw_input().split(' '))
res = a * b * (1 if a < 10 and b < 10 else 0)
print res if res else -1