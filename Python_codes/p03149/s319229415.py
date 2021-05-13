from sys import exit, stdin
N = set([int(_) for _ in stdin.readline().rstrip().split()])
if N == set([1,9,7,4]):
    print('YES')
else:
    print('NO')