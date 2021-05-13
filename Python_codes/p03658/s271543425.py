# ABC 067 B
N,K = map(int,input().split())
L =[int(i) for i in input().split()]
L.sort(reverse=True)
ans = sum(L[:K])
print(ans)