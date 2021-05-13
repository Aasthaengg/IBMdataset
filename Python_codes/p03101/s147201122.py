H, W = map(int, input().split())
x, y = map(int, input().split())

print(H*W - W*x - (H-x)*y)
