import sys
def S(): return sys.stdin.readline().rstrip()


S = S()
print(S+'es' if S[-1] == 's' else S+'s')
