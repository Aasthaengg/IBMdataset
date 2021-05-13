s=list(input())
t=list(input())
s.sort()
t.sort(reverse=True)
s_="".join(s)
t_="".join(t)
if s_<t_:
    print("Yes")
else:
    print("No")