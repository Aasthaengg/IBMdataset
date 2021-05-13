N,M = map(int,input().split())
H_list = list(map(int,input().split()))
A_list = [0] * M
B_list = [0] * M
C_list = [0] * N
for i in range(M):
    A_list[i],B_list[i] = map(int,input().split())
for a,b in zip(A_list,B_list):
    if H_list[a-1] < H_list[b-1]:
        C_list[a-1] = -1
    elif H_list[a-1] > H_list[b-1]:
        C_list[b-1] = -1
    elif H_list[a-1] == H_list[b-1]:
        C_list[a-1] = C_list[b-1] = -1
print(C_list.count(0))