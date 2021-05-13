#ABC067.B
N,K = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
L = l[(N-K):]
ans = sum(L)
print(ans)