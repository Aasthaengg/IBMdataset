s = input()
t = input()
l_s = len(s)
l_t = len(t)

s2 = s + s
l_s2 = len(s2)

next_idx_1 = [[l_s2] * 26 for i in range(l_s2+1)]

for i in reversed(range(l_s2)):
    for j in range(26):
        next_idx_1[i][j] = next_idx_1[i+1][j]
    next_idx_1[i][ord(s2[i]) - ord("a")] = i

next_idx_2 = [[l_s2] * 26 for i in range(l_s2)]

for i in reversed(range(1, l_s2)):
    for j in range(26):
        next_idx_2[i-1][j] = next_idx_2[i][j]
    next_idx_2[i-1][ord(s2[i]) - ord("a")] = i

cur_idx = 0
for i in range(l_t):
    if i == 0:
        idx = next_idx_1[cur_idx%l_s][ord(t[i]) - ord("a")]

    else:
        idx = next_idx_2[cur_idx%l_s][ord(t[i]) - ord("a")]

    if idx == l_s2:
        print("-1")
        exit()

    cur_idx += idx - (cur_idx % l_s)
    
print(cur_idx+1)