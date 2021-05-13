import sys
input = sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))

print(sum(a)-N)