import sys
input = sys.stdin.readline


N = int(input())
d = dict()

for _ in range(N):
    op, key = input().strip().split()
    if op == "insert":
        d[key] = True
    elif op == "find" and key in d.keys():
        print("yes")
    else:
        print("no")

