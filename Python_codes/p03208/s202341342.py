N,K = map(int,input().split())
H = []
for i in range(N):
    h = int(input())
    H.append(h)
H.sort()
ans = 1000000000
for i in range(N-K+1):
    tmp = H[K-1+i] - H[i]
    if tmp < ans:
        ans = tmp
print(ans)