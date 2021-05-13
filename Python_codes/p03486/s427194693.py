s_lst = list(input())
t_lst = list(input())
s_lst.sort()
t_lst.sort(reverse = True)
s = ""
for ss in s_lst:
    s += ss
t = ""
for tt in t_lst:
    t += tt

if s < t:
    print("Yes")
else:
    print("No")
