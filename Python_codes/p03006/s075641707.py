n = int(input())
all_li = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    all_li.append(tmp)
if len(all_li) == 1:
    print(1)
    exit()
lee = len(all_li)
vector_map = {}
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a = all_li[i][0]
        b = all_li[i][1]
        c = all_li[j][0]
        d = all_li[j][1]
        if (c-a,d-b) in vector_map:
            vector_map[(c-a,d-b)] += 1
        else:
            vector_map[(c-a,d-b)] = 1
m = max(vector_map.values())
print(n-m)