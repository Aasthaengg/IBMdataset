def readints():
    return list(map(int, input().split()))


a, b, c = map(int, input().split())
print("Yes" if a+b >= c else "No")
