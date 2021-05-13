import sys
N = int(input())
if N < 100 or N > 1000:
    sys.exit()
strN = str(N)
if N == int(strN[::-1]):
    print("Yes")
else:
    print("No")