import sys
# input = sys.stdin.readline
N, K = map(int, input().split())
td = [list(map(int, input().split())) for _ in range(N)]

table = [[] for _ in range(N)]
for i, (ti, di) in enumerate(td):
    table[ti - 1].append((i, ti, di))

tops = []
others = []
for row in table:
    if len(row) > 0:
        for i, item in enumerate(sorted(row, key=lambda x: -x[2])):
            if i == 0: tops.append(item)
            else: others.append(item)

tops.sort(key=lambda x: -x[2])
others.sort(key=lambda x: -x[2])
x_max = len(tops)

tops_sumtab = [0]
tmp = 0
for i, ti, di in tops:
    tmp += di
    tops_sumtab.append(tmp)
    
others_sumtab = [0]
tmp = 0
for i, ti, di in others:
    tmp += di
    others_sumtab.append(tmp)

# print("#", tops)
# print("#", others)
ans = 0
for i in range(K + 1):
    if K - i > len(others): continue
    elif i > len(tops): break
    # print("##", tops_sumtab[i], others_sumtab[K - i], i ** 2)
    ans_tmp = tops_sumtab[i] + others_sumtab[K - i] + i ** 2
    if ans < ans_tmp: ans = ans_tmp

print(ans)