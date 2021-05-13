s = str(input())
t = str(input())

s_str = sorted(s)
t_str = sorted(t, reverse=True)

if(s_str < t_str):
    print('Yes')
else:
    print('No')
