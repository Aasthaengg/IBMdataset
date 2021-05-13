x, y = map(int, input().split())

f = lambda x: 10**10 if x < 0 else x

print(min(f(y-x), f(y+x)+1, f(-y-x)+1, f(-y+x)+2))