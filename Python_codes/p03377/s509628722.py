def readints():
    return list(map(int, input().split()))


A, B, X = map(int, input().split())
if A+B < X:
    print("NO")
    exit()
if A > X:
    print("NO")
    exit()
print("YES")
