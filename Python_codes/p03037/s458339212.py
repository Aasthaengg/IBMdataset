N,M = map(int,input().split())
LR = [list(map(int,input().split()))for _ in range(M)]

L,R = list(zip(*LR))#転置
#print(L)
#print(R)
print(max(min(R)-max(L)+1,0))

