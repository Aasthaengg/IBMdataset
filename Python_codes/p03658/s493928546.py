N,K = map(int,input().split())
L = list(map(int,input().split()))
L.sort()
ans = sum(L[::-1][:K])
print(ans)