N=int(input())
H=list(map(int,input().split()))
min = 1e12
success = True
for i in range(N):
    if H[N-1-i] <= min + 1:
        if H[N-1-i] < min:
            min = H[N-1-i]
    else:
        success = False
        break
print('Yes' if success else 'No')
