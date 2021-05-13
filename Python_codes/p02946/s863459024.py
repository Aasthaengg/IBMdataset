K,X=[int(x) for x in input().rstrip().split()]
left=X-K+1
right=X+K
l=[i for i in range(left,right)]
print(*l)