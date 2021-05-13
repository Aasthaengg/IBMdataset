import sys
input = sys.stdin.readline

A = sorted(list(map(int,input().split())))
subA = A[2]-A[1]+A[2]-A[0]
print(subA//2 + subA%2*2)
