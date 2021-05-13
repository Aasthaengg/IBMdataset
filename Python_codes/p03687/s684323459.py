s = input()
se = set(list(s))
# print('se', se)

if len(se) == 1:
    print(0)
    exit()


def f(v):
    s_list = s.split(v)
    s_list = [len(i) for i in s_list if i]
    return max(s_list)


ans = 1000
for i in se:
    v = f(i)
    ans = min(ans, v)
print(ans)
# serval 6,1
# srvvl  5,2
#        4,3

#  → svvv → vvv

# jackal
# aacaa

# jaajjj
# aaajj
# aaaj
# aaa

# jajjjjjjjajjjjjjjjjj
# aajjjjjjaajjjjjjjjj
# aajjjjjaaajjjjjjjj
# aajjjjaaaajjjjjjj
# ...
