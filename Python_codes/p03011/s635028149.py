import sys
input = sys.stdin.readline

P=list(map(int,input().split()))
print(sum(P)-max(P))

