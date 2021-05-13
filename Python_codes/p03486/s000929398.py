s=input()
t=input()
s_list=sorted(s)
t_list=sorted(t)
t_list.reverse()
s2="".join(s_list)
t2="".join(t_list)
if  s2<t2:
    print("Yes")
else:
    print("No")
