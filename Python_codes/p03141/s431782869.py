n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
sum_ab = [(i, v[0]+v[1]) for i, v in enumerate(ab)]
sum_ab.sort(key=lambda x: x[1], reverse=True)
t_res = 0
a_res = 0
for i,v in enumerate(sum_ab):
    if i % 2 == 0:
        t_res += ab[v[0]][0]
    else:
        a_res += ab[v[0]][1]
print(t_res-a_res)