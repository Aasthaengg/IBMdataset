N = int(input())
H = list(map(int,input().split()))

#height = H[0]
index = 0
maximum = 0
for i in range(1,N):
    if H[i-1] < H[i]:
        maximum = max(maximum,i-1-index)
        index = i 
    elif i == N-1:
        maximum = max(maximum,i-index)
print(maximum)