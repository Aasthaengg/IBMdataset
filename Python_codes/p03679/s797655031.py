X, A, B =map(int, input().split())

limit=B-A

# おしいくないが、お腹壊さない
if A>=B:
    print("delicious")
elif B-A<=X:
    print("safe")
elif B-A>X:
    print("dangerous")