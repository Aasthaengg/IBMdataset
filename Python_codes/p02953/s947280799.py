import sys
N = int(input())
H = list(map(int, input().split()))

H.reverse()
for n in range(1, N):
    if H[n]-H[n-1]==1:
        H[n] -= 1
    elif H[n]-H[n-1] > 1:
        print("No")
        sys.exit(0)
print("Yes")