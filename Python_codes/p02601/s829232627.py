import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
X = list(map(int,input().split()))
K = int(input())
K += 1

for i in range(K):
    for j in range(K-i):
        for k in range(K-i-j):
            if X[0]*(2**i) < X[1]*(2**j) and X[1]*(2**j) < X[2]*(2**k):
                print('Yes')
                sys.exit()
print('No')

