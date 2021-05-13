N,K=map(int,input().split())
l=[int(i) for i in input().split()]
l.sort()
l=l[N-K:]
print(sum(l))