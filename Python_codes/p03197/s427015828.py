from sys import stdin
n = int(stdin.readline().rstrip())
li = [int(stdin.readline().rstrip()) for _ in range(n)]
if all(i%2 == 0 for i in li):
    print("second")
else:
    print("first")