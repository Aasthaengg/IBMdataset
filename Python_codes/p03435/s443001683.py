C_list=[]
for _ in range(3):
    C_list.append(list(map(int,input().split())))

from itertools import combinations

ans='Yes'
for r in combinations(range(3),2):
    for c in combinations(range(3),2):
        if C_list[r[0]][c[0]]-C_list[r[1]][c[0]] != C_list[r[0]][c[1]]-C_list[r[1]][c[1]]:
            ans='No'
            break
        if C_list[r[0]][c[0]]-C_list[r[0]][c[1]] != C_list[r[1]][c[0]]-C_list[r[1]][c[1]]:
            ans='No'
            break
print(ans)