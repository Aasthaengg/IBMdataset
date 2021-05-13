N = int(input())
N_List = []
for i in range(N):
    N_List.append(int(input()))

maxN = max(N_List)
N_List.pop(N_List.index(maxN))
print(sum(N_List) + int(maxN/2))