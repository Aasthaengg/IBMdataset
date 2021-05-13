a, b, c = map(str, input().split())
max = int(a+b) + int(c)
if max < int(a) + int(b+c):
    max = int(a) + int(b+c)

elif max < int(c+a) + int(b):
    max = int(c+a) + int(b)
print(max)