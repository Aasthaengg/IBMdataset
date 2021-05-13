n,k=map(int,input().split())
l=sorted([int(s) for s in input().split()])
print(sum(l[k*(-1):]))