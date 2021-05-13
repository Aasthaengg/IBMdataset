n, m, p = [ int(v) for v in input().split() ]
node_list = []
node_list_2 = []
for i in range(m):
    a, b, c = [ int(v) for v in input().split() ]
    node_list.append((a-1,b-1,p-c))
    node_list_2.append((b-1,a-1,p-c))


def b_f(node_list,n,t):
    distance_list = [ 10**15 for i in range(n) ]
    distance_list[t] = 0

    for i in range(n):
        new_distanece_list = distance_list
        for j in node_list:
            a, b, c = j
            if distance_list[a] != 10**15:
                if new_distanece_list[b] > distance_list[a] + c:
                    new_distanece_list[b] = distance_list[a] + c
        distance_list = new_distanece_list

        if i == n-2:
            distance_list_n_minus_1 = [i for i in distance_list]
        elif i == n-1:
            distance_list_n = [i for i in distance_list]

    if distance_list_n_minus_1 == distance_list_n:
        negative_cycle = 0
    else:
        negative_cycle = 1

    return distance_list_n_minus_1, negative_cycle


point_list_s = b_f(node_list,n,0)[0]
point_list_g = b_f(node_list_2,n,n-1)[0]
point_list = [ True for i in range(n) ]

for i in range(n):
    if point_list_s[i] == 10**15 or point_list_g[i] == 10**15:
        point_list[i] = False

node_list_3 = [ i for i in node_list if point_list[i[0]] == True and point_list[i[1]] == True ]
ans = b_f(node_list_3,n,0)

if ans[1] == 0:
    print(-min(0,ans[0][-1]))
else:
    print(-1)