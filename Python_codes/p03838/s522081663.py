x, y = map(int, input().split())
print(min(y-x, abs(y+x)+1) if x<y else min(-y+x+2, abs(y+x)+1))
