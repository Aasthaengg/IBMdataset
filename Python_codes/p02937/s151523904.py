from bisect import bisect_left, bisect_right

s = input()
t = input()

alp = 'abcdefghijklmnopqrstuvwxyz'
alp_pos = {}
for a in alp:
    alp_pos[a] = []

for i,v in enumerate(s):
    alp_pos[v].append(i+1)


loop = 0
curr_pos = 0
for ti in t:
    if not alp_pos[ti]:
        print(-1)
        exit()
    curr_alp_poss = alp_pos[ti]
    ind = bisect_right(curr_alp_poss, curr_pos)
    if ind >= len(curr_alp_poss):
        loop += 1
        curr_pos = curr_alp_poss[0]
    else:
        curr_pos = curr_alp_poss[ind]

print(loop*len(s)+curr_pos)

