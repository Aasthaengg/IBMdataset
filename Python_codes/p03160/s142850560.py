import sys
input = sys.stdin.readline
n = int(input())
H = list(map(int,input().split()))

D = [float("inf") for i in range(n)]
D[0] = 0
for i in range(1, n):
    for j in range(1, 3):
        if i-j >= 0:
            D[i] = min(D[i], D[i-j]+abs(H[i]-H[i-j]))
    
print(D[-1])