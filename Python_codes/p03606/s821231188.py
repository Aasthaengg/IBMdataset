n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
print(sum(list([A[1]-A[0]+1 for A in l])))