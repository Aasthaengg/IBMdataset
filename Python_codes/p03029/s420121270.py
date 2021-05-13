import sys
input = lambda : sys.stdin.readline().rstrip()

a, p = [int(x) for x in input().split()]
print((3*a + p) // 2)