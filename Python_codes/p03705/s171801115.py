import sys
input = sys.stdin.readline

N,A,B = list(map(int,input().split()))
min_sum = A*(N-1)+B
max_sum = B*(N-1)+A
print(max(0,max_sum-min_sum+1))