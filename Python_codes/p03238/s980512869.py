from sys import stdin
import bisect

n = int(stdin.readline().rstrip())

if n == 1:
    print("Hello World")
    exit()

li = [int(stdin.readline().rstrip()) for _ in range(n)]

print(sum(li))