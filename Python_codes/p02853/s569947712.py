X, Y = map(int, input().split())
print(max(0, (4-X)*100000) + max(0, (4-Y)*100000) + max(0, (3-X-Y)*400000))