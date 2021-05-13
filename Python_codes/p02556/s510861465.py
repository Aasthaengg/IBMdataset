N = int(input())
i = 0
a_max = 2
a_min = 2*(10**9)
s_max = 1-10**9
s_min = 10**9-1

for i in range(N):
    x,y=map(int,input().split())
    add = x+y
    sub = x-y

    if add > a_max:
        a_max = add
    if add < a_min:
        a_min = add
    
    if sub > s_max:
        s_max = sub
    if sub < s_min:
        s_min = sub

d_add = a_max - a_min
d_sub = s_max - s_min

#if d_add >= d_sub:
#    print(d_add)
#if d_add < d_sub:
#    print(d_sub)
print(max(d_add,d_sub))