x, y = map(int, input().split())
print(min(abs(~x+y), abs(y+x))+1)
