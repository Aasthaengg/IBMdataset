K,S = map(int,input().split())
print(sum([0<=S-X-Y<=K for X in range(K+1) for Y in range(K+1)]))