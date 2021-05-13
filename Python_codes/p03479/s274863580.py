x, y = map(int, input().split())
r = 1
while x*(2**r) <= y:
    r += 1

print(r)