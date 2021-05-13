def readints():
    return list(map(int, input().split()))


a, b = map(int, input().split())
if a == b:
    print(a)
    exit()
if a > b:
    print(a-1)
if a < b:
    print(a)
