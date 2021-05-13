s, t = input().split()
s_num , t_num = map(int, input().split())
u = input()

if u == s:
    print(s_num-1, t_num)
else:
    print(s_num, t_num -1)