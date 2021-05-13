x, y = map(int, input().split())
if max(x, y) - 2 >= min(x, y):
    print(max(x,y)*2-1)
else:
    print(max(x, y) + min(x, y))
