import sys
input = sys.stdin.readline
X, A, B = [int(x) for x in input().split()]
if (A - B) >= 0:
    print("delicious")
elif (B - A) <= X:
    print("safe")
else:
    print("dangerous") 