N, M = map(int, input().split())

p_list = []
s_list = []
for i in range(M):
    p, s = input().split()
    p_list.append(int(p))
    s_list.append(s)

p_state = [0 for i in range(N)]
pena_list = [0 for i in range(N)]
ans = 0
pena = 0

for i in range(M):
    if p_state[p_list[i]-1] == 0 and s_list[i] == "WA":
        pena_list[p_list[i]-1] += 1
    elif p_state[p_list[i]-1] == 0 and s_list[i] == "AC":
        p_state[p_list[i]-1] = 1
        ans += 1
        pena += pena_list[p_list[i]-1]
    else:
        continue

print(ans, pena)
