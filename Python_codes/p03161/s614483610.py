import sys
input = sys.stdin.readline
n, k = map(int, input().split())
H = list(map(int,input().split()))

# from random import randint
# n = 10**5
# k = 100
# H = [randint(1, 10**4) for i in range(n)]

D = [float("inf") for i in range(n)]
D[0] = 0
for i in range(1, n):
    for j in range(1, k+1):
        if i-j >= 0:
            D[i] = min(D[i], D[i-j]+abs(H[i]-H[i-j]))
    
print(D[-1])