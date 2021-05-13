N=int(input())
A=[int(input()) for _ in range(N)]
tab = [0]*N
prev=10**10
for i,a in enumerate(A):
    dst = i-a
    if dst < 0 or dst >=N or (a>prev and a-prev>1):
        print(-1)
        exit()
    tab[dst] = max(tab[dst], a)
    prev = a
print(sum(tab))
