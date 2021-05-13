X, A, B = map(int, input().split())
eat = B-A

if A >= B:
    print("delicious")
elif eat >= X+1:
    print("dangerous")
else:
    print("safe")