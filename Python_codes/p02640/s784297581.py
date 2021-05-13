x, y = map(int, input().split())
print("YNeos"[1 - (x * 2 <= y <= x * 4 and y % 2 == 0)::2])