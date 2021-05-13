X, A, B = map(int, input().split())
if B <= A:
    print("delicious")
else:
    if (B-A) <= X:
        print("safe")
    if (B-A) > X:
        print("dangerous")