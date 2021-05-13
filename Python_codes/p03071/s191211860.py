A, B = map(int, input().split())
botan = [A, A-1, B, B-1]
botan.sort()
print(botan[-1]+botan[-2])