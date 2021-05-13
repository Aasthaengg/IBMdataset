N_List = list(map(int,input().split()))
N_List.insert(0,N_List.pop(2))
print(" ".join(map(str,N_List)))