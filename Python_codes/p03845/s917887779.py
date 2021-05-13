N=int(input())
T_list=list(map(int,input().split()))
M=int(input())
tmp=[list(map(int,input().split())) for i in range(M)]
for i in range(M):
    print(tmp[i][1]+sum(T_list)-T_list[tmp[i][0]-1])
