N, K = map(int,input().split())
H=[]
for i in range (N):
    h=int(input())
    H.append(h)

H = sorted(H)
ans = H[K-1] - H[0]
for i in range (N-K+1):
    ans = min (ans, H[i+K-1]-H[i])

print(ans)