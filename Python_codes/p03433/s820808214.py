import sys
n = int(sys.stdin.readline())
a = int(sys.stdin.readline())

if n % 500 <= a:
    print("Yes")
else:
    print("No")
