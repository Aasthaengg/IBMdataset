N, M = map(int, input().split())
H = list(map(int, input().split()))

ap = [False]*(N+1)

for m in range(M):
    a, b = map(int, input().split())
    if H[a-1] > H[b-1]: 
        ap[b] = True
    elif H[a-1] < H[b-1]:
        ap[a] = True
    elif H[a-1] == H[b-1]:
        ap[a] = True
        ap[b] = True

count = 0
for a in range(1, N+1):
    if ap[a] == False:
        count += 1

print(count)