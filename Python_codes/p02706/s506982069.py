n,m=map(int,input().split())
a=[int(i) for i in input().split()]
print(max(-1,(n-sum(a))))
