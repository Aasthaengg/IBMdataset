import sys

input()
print('\n'.join('YES' if t[0] ** 2 + t[1] ** 2 == t[2] ** 2 else 'NO' for t in
                [sorted(map(int, l.split())) for l in sys.stdin]))