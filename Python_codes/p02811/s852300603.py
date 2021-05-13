import sys
input = sys.stdin.readline

K,X = list(map(int,input().split()))
print('Yes' if 500*K >=X else 'No')
