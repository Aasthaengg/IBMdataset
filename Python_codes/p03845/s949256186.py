N=int(input())
T=list(map(int,input().split()))
total = sum(T)
M=int(input())
for _ in range(M):
    p,x = map(int,input().split())
    reduced = T[p-1]-x
    print(total - reduced)