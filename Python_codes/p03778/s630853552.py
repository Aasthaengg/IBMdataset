W, A, B = map(int, input().split())
if B > A+W:
    print(B-A-W)
elif A > B+W:
    print(A-B-W)
else:
    print(0)