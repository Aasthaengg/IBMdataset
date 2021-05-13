n, w = map(int, input().split())
V = [list(map(int, input().split())) for i in range(n)]

w0 = V[0][0]

V_split = [[] for i in range(4)]
for i in range(n):
    V_split[V[i][0] - w0].append(V[i][1])

for i in range(4):
    V_split[i].sort(reverse=True)

# print(V_split)

V_split_S = [[0] for i in range(4)]
for i in range(4):
    for j in range(len(V_split[i])):
        V_split_S[i].append(V_split_S[i][-1] + V_split[i][j])

# print(V_split)
# print(V_split_S)


ans = 0

for i in range(min(len(V_split_S[0]), w//w0 + 1)):
    wi = w - w0 * i
    for j in range(min(len(V_split_S[1]), wi//(w0+1) + 1)):
        wj = wi - (w0+1) * j
        for k in range(min(len(V_split_S[2]), wj//(w0+2) + 1)):
            wk = wj - (w0+2) * k
            l = min(len(V_split_S[3]), wk//(w0+3) + 1) - 1
            
            ans = max(ans, V_split_S[0][i] + V_split_S[1][j] + V_split_S[2][k] + V_split_S[3][l])
            # print(i,j,k,l, ans)
print(ans)
