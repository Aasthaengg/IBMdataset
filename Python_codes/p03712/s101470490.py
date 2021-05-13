h, w = map(int, input().split())

sh = '#'

print(sh * (w+2))
[print(sh + input() + sh) for i in range(h)]
print(sh * (w+2))