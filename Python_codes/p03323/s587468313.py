import sys
def input(): return sys.stdin.readline().rstrip()
A, B = map(int, input().split())
print(':(' if A > 8 or B > 8 else 'Yay!')