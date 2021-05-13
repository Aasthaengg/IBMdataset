import sys
input = sys.stdin.readline

c1 = input().rstrip()
c2 = input().rstrip()[-1::-1]

print('YES' if c1 == c2 else 'NO')
