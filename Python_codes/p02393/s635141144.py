a, b, c = map(int, input().split())
numlist = [a, b, c]
numlist.sort()
print(" ".join(map(str, numlist)))