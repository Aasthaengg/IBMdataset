N,M = map(int,input().split())
for i in range(M):
    st,sp = map(int,input().split())
    if i == 0:
        N_List = [st,sp]
    else:
        if st > N_List[0]:
            N_List[0] = st
        if sp < N_List[1]:
            N_List[1] = sp   
print(len(list(range(N_List[0],N_List[1]+1))))