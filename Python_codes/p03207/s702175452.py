N = int(input())

p = []
for i in range(N):
    p.append(int(input()))

saidai = max(p)
del p[p.index(saidai)]
print(sum(p)+ saidai//2)