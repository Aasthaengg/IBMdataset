def li():
    return list(map(int, input().split()))


def mi():
    return map(int, input().split())


def ii():
    return int(input())


A, B, X = mi()

if X < A:
    print("NO")
elif X - A <= B:
    print("YES")
else:
    print("NO")
