n=int(input())
s_list=[]
t_list=[]
for i in range(n):
    s,t=input().split()
    t=int(t)
    s_list.append(s)
    t_list.append(t)
x =input()
print(sum(t_list[s_list.index(x):])-t_list[s_list.index(x)])