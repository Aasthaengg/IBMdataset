from bisect import bisect_left, bisect_right
s = input()
t = input()
n_s = len(s)
n_t = len(t)


idx = [[] for _ in range(26)]
#print(ord("a"))
#print(ord("z"))

def a_idx(a):
    idx = ord(a)
    idx -= 97
    return idx


for i in range(n_s):
    idx[a_idx(s[i])].append(i)

t_syutugenkasyo = []
for i in range(n_t):
    t_syutugenkasyo.append(idx[a_idx(t[i])])
#print(t_syutugenkasyo)

now = -1
ans = 0
for i in range(n_t):
    if len(t_syutugenkasyo[i]) == 0:
        print(-1)
        exit()
    ni = bisect_right(t_syutugenkasyo[i], now)
    if ni >= len(t_syutugenkasyo[i]):
        ans += n_s
        now = t_syutugenkasyo[i][0]
    else:
        now = t_syutugenkasyo[i][ni]
ans += now+1
print(ans)