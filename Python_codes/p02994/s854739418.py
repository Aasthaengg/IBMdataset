N,L = map(int, input().split())
r = [L+i-1 for i in range(1,N+1)]
e = min(r, key=abs)
print(sum(r)-e)