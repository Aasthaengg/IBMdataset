n,k = map(int,input().split())
L = list(map(int,input().split()))
L.sort(reverse=True)
ans = sum(L[0:k])
print(ans)
