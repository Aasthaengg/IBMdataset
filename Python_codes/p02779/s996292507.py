import sys
input = sys.stdin.readline

n, s = int(input()), list(map(int, input().split()))
print('YES' if len(set(s)) == len(s) else 'NO')