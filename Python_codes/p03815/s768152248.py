import sys
input = sys.stdin.readline

x = int(input())

if not x % 11:
    print(x // 11 * 2)
elif x % 11 <= 6:
    print(x // 11 * 2 + 1)
else:
    print(x // 11 * 2 + 2)
