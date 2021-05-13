N = int(input())
H = list(map(int,input().split()))
b = [0]*N
mb = 0
for i in range(N-2,-1,-1):
    if H[i+1] <= H[i]:
        b[i] = b[i+1]+1
    else:
        b[i]= 0
    mb = max(mb,b[i])
print(mb)
