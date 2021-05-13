a,b = map(int, raw_input().split())
og = b - a - 1
print og * (og + 1) / 2 - a
