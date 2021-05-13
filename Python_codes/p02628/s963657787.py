N,K = map(int,input().split())
array = sorted(list(map(int,input().split())))
ans = sum(array[0:K])
print(ans)