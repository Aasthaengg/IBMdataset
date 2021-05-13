N = int(input())
N_List = list(map(int,input().split()))
ct = 0
for i in range(1,N-1):
    if (N_List[i] > N_List[i-1]) & (N_List[i] < N_List[i+1]):
        ct += 1
    elif (N_List[i] < N_List[i-1]) & (N_List[i] > N_List[i+1]):
        ct += 1


print(ct)
