import itertools

N, M, Q = map(int, input().split())
abcd_list = [ list(map(int, input().split())) for _ in range(Q) ]

com_list = list(itertools.combinations_with_replacement(range(M), N))
ans = 0
for com in com_list:
    tmp = 0
    for abcd in abcd_list:
        if (com[abcd[1]-1] - com[abcd[0]-1]) == abcd[2]:
            tmp += abcd[3]
    ans = max(ans, tmp)
print(ans)