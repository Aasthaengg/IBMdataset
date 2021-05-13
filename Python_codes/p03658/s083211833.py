a, b = map(int, input().split())
length = map(int, input().split())
length = sorted(length, reverse=True)

print(sum(length[:b]))