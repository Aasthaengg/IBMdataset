a, b, c, d = list(map(int, input().split()))
if a + b == c + d:
    print('Balanced')
    exit()
print('Left') if a + b > c + d else print('Right')
