x, a, b = map(int, input().split())
ax = int((((a-x)**2)**0.5)//1)
bx = int((((b-x)**2)**0.5)//1)
print('A') if ax < bx else print('B')