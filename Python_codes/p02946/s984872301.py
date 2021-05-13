K,X=map(int,input().split())
l=[int(x) for x in range(X-(K-1),X+K)]
print(*l)