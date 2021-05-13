h, w = map(int, input().split())
sh, sw = map(int, input().split())

dup = sh*sw
black = sh*w + sw*h - dup
white = h*w - black

print(white)