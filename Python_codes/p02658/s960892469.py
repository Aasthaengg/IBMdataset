from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

ans = 1

if 0 in A:
    ans = 0

if ans:
    for a in A:
        ans *= a
        if ans > pow(10, 18):
            ans = -1
            break

print(ans)