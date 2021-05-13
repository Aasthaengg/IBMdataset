import sys
input = sys.stdin.readline

N,A,B = list(map(int,input().split()))
print(N*A if N*A<B else B)
