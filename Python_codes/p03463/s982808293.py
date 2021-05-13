N, A, B = map(int, input().split())

AliceWin = False
C = B - A - 1
if C % 2 == 1:
    AliceWin = True

if AliceWin:
    print("Alice")
else:
    print("Borys")
