N=int(input());T=list(map(int,input().split()));M=int(input());total=sum(T)
px=[list(map(int,input().split())) for _ in range(M)]
[print(total + px[i][1] - T[px[i][0]-1]) for i in range(M)]