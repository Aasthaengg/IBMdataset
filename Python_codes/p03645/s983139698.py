N,M=map(int,input().split())
AB=[[] for i in range(N)]
for j in range(M):
    a,b=map(int,input().split())
    AB[a-1].append(b)
    AB[b-1].append(a)
for ab in AB:
    if 1 in ab and N in ab:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")