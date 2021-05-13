a,b,c,d = tuple(map(int, input().split(" ")))

print(max(a*c, a*d, b*c, b*d))