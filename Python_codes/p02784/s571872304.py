import sys
input = sys.stdin.readline
H,N = list(map(int,input().split()))
A = list(map(int,input().split()))
print('Yes' if sum(A)>=H else 'No')