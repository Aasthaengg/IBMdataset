X, A, B = map(int, input().split())
if A >= B:
    print("delicious")
elif A + X + 1 > B:
    print("safe")
else:
    print("dangerous")
