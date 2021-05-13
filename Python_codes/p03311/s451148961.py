N=int(input())
*A,=map(int,input().split())
B=[A[i]-(i+1) for i in range(N)]
B.sort()
b=B[N//2]
print(sum(abs(bb-b)for bb in B))