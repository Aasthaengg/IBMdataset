n,k = map(int,input().split())
print(max(n-k,1) if k > 1 and k != n else 0)