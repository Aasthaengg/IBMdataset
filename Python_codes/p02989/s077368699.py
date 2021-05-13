N = int(input())
N_List = sorted(list(map(int,input().split())))
std = int(N/2)
ansstd = N_List[std] - N_List[std-1] 
print((0,ansstd)[ansstd > 0])