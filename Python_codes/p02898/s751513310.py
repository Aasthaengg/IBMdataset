_, K = map(int, input().split())
print(len([int(x) for x in input().split() if int(x) >= K]))

