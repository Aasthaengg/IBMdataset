H, M, h, m, k = map(int, input().split())
print(60*(h-H) + (m-M) - k)