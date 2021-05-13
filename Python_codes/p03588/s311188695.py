import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

A.sort()
print(A[-1][0] + A[-1][1])