L=list(map(int,input().split()))
print(min(sum(L)-v for v in L))
