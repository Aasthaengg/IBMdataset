X, A, B = map(int, input().split())

if B <= A:
    print("delicious")
elif B <= (X + A):
    print("safe")
elif B >= (X + A + 1):
    print("dangerous")
