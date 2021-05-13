N,K=map(int,input().split())
*H,=map(int,input().split())

H.sort()
print(sum(H[:max(N-K,0)]))