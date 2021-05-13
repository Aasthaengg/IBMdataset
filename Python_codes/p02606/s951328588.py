import sys
l,r,d = map(int, sys.stdin.readline().rstrip("\n").split())
q1 = (l-1) // d
q2 = r // d
print(q2-q1)