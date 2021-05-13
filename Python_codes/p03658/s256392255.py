import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))
l=sorted(list(map(int,input().split())),reverse=1)
print(sum(l[:k]))