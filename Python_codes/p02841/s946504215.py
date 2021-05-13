import sys
read = sys.stdin.read

M, D, m, d = map(int, read().split())
if M != m:
    print(1)
else:
    print(0)