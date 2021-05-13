n, a, b, c = [int(x) for x in input().split()]
l_list = [int(input()) for _ in range(n)]

s_list = [a, b, c]

ans = 10000
for i in range(4 ** n):
    mp = 0
    temp_l_list = [0, 0, 0]
    
    for j in range(n):
        temp = (i >> (2 * j)) & 3
        if temp == 3:
            continue

        if temp_l_list[temp] != 0:
            mp += 10
        temp_l_list[temp] += l_list[j]

    for s, temp_l in zip(s_list, temp_l_list):
        if temp_l == 0:
            break
        mp += abs(s - temp_l)
    else:
        if ans > mp:
            ans = mp
print(ans)