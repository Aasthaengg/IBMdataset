import sys
stdin=sys.stdin

ns = lambda:stdin.readline().rstrip()
ni = lambda:int(stdin.readline().rstrip())
nm = lambda:map(int,stdin.readline().split())
nl = lambda:list(map(int,stdin.readline().split()))

N=int(input())
print((N*(N-1)//2))  