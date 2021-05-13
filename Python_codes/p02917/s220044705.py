from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n = int(input()) - 1
ar = [int(i) for i in input().split()]
sm = ar[0]
for i in range(1, n):
    sm += min(ar[i], ar[i - 1])
sm += ar[n - 1]
print(str(sm))