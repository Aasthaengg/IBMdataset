n = int(input())
import sys
an = list(map(int, sys.stdin.readline().split()))

if len(set(an))==n:
    print('YES')
    exit(0)

print('NO')