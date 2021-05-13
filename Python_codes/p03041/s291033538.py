import sys

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


n, k = nm()
k -= 1
S = list(input())
S[k] = S[k].lower()
print(''.join(S))