import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


S = li()
if len(S) == 2:
    print(''.join(S))
else:
    S.reverse()
    print(''.join(S))