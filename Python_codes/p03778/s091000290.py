w, a, b = map(int, input().split())
x = max(a, b)
y = min(a, b)
print(max((x - (y + w)), 0 ))