a, b, c = map(int, input().split())
maxx = max(a, b, c)
red = (maxx // 2 * a * b * c // maxx)
blue = a * b * c - red
print(blue - red)