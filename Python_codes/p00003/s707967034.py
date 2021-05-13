import sys

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    l1,l2,l3 = sorted(map(int, sys.stdin.readline().rstrip().split(' ')))
    print("YES" if (l1**2 + l2**2 == l3**2) else "NO")