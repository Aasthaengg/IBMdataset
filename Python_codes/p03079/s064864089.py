import sys
stdin = sys.stdin
read_int = lambda : list(map(int,stdin.readline().split()))
read_str = lambda : stdin.readline().rstrip()

A,B,C = read_int()

if A == B and B == C:
    print('Yes')
else:
    print('No')
