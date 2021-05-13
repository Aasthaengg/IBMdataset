#https://atcoder.jp/contests/abc078/tasks/abc078_c
N = int(input())
N_List = sorted(list(map(int,input().split())))
for i in range(N-1):
    Current_N = (N_List[0]+N_List[1])/2
    del N_List[0:2]
    N_List.insert(0,Current_N)

     
print(N_List[0])