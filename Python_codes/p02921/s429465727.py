import sys
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

S=list(input())
T=list(input())

print(sum([1 for x,y in zip(S,T) if x==y]))
