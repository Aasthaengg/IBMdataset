def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


N = ii()
A = ii()

modN500 = N % 500

if modN500 <= A:
    print("Yes")
else:
    print("No")
