N,K = map(int,input().split())
N_List = map(int,input().split())
ans = [i for i in N_List if i >= K]
print(len(ans))