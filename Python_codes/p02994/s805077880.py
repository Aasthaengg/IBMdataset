N,L=map(int,input().split())
all = sum([L+i-1 for i in range(1, N+1)])
anss = []
for j in range(1, N+1):
    tmp = sum([L+i-1 for i in range(1, N+1) if i != j])
    anss.append((abs(all-tmp), tmp))
anss.sort()
print(anss[0][1])
