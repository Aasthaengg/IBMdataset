cube = list(map(int, input().split()))
cube.sort()
if any([i % 2 == 0 for i in cube]):
    print(0)
else:
    print(cube[0] * cube[1])