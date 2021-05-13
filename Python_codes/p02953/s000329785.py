import sys

N = int(input())
H = list(map(int, input().split()))

H = H[::-1]

for i in range(N-1):
    if H[i+1] - H[i] > 1:
        print('No')
        sys.exit()
    elif H[i+1] - H[i] == 1:
        H[i+1] -= 1
    else:
        pass    

print('Yes')