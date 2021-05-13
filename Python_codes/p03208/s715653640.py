N,K=map(int,input().split())
H=[]
for _ in range(N):
    H.append(int(input()))
H.sort()
min = 1e12
for i in range(N-(K-1)):
    diff = H[i+K-1] - H[i]
    if diff < min:
        min = diff

print(min)