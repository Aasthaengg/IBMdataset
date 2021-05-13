N = int(input())
L = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):

            edge_list = sorted([L[i], L[j], L[k]])
            if edge_list[0] != edge_list[1] != edge_list[2] and edge_list[2] < edge_list[0] + edge_list[1]:

                ans += 1


print(ans)