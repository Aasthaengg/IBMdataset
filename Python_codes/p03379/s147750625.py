import sys
input = sys.stdin.readline

N = int(input())
X =list(map(int,input().split()))
sX = sorted(X)
med_s = sX[((N-1)+1)//2-1]
med_b = sX[((N-1)+1)//2]
ave_med = (med_s+med_b)/2

for i in range(N):
    if X[i] <= ave_med:
        print(med_b)
    else:
        print(med_s)
