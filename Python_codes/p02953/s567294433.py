import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

H[0] -= 1
left = 0
for i in range(N):
    if left > H[i]:
        print("No")
        exit()
    elif H[i] > left:
        left = H[i] - 1
    else:
        left = H[i]
print("Yes")
