W, H, x, y = map(int,input().split())

print("{0} {1}".format(W*H/2, (int)(x==W//2 and y==H//2 and W % 2 == 0 and H % 2 == 0)))