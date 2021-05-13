N,K=map(int,input().split())
p=sorted(list(map(int,input().split())))
all=0
for i in range(K):
    all+=p[i]
print(all)