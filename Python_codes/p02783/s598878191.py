H, A = map(int, input().split())
res = H // A + (H % A > 0)
print(res)