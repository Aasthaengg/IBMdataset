def readints():
    return list(map(int, input().split()))


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min(a, b)+min(c, d))
