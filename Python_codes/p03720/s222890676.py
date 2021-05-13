N,M= map(int,input().split())
AB = [list(map(lambda x:x-1,[int(i) for i in input().split()])) for _ in range(M)]
c = [0]*N

for i in range(M) :
    c[AB[i][0]] += 1
    c[AB[i][1]] += 1

for i in range(N) :
    print(c[i])