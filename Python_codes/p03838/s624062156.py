x, y = map(int, input().split())
print(min(y+~x+1, abs(y+x)+1) if x<y else min(-~x-y+1, abs(y+x)+1))
