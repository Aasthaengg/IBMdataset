n,k=map(int,input().split())
L = sorted(list(map(int,input().split())))[::-1]
print(sum(L[0:k]))