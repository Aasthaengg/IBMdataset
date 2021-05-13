n = int(input())

t_list = [ int(v) for v in input().split() ]
a_list = [ int(v) for v in input().split() ]
a_list_reverse = list(reversed(a_list))

t_confirm_list = [t_list[0]] + [None for i in range(n-1)]
a_confirm_list = [a_list_reverse[0]] + [None for i in range(n-1)]


for i in range(n-1):
    if t_list[i]  < t_list[i+1]:
        t_confirm_list[i+1] = t_list[i+1]
    if a_list_reverse[i]  < a_list_reverse[i+1]:
        a_confirm_list[i+1] = a_list_reverse[i+1]

a_confirm_list.reverse()


mod = 10**9+7
ans = 1
for i in range(n):
    if a_confirm_list[i] != None and t_confirm_list[i] != None:
        if a_confirm_list[i] != t_confirm_list[i]:
            ans = 0
    elif a_confirm_list[i] == None and t_confirm_list[i] == None:
        ans *= min(a_list[i],t_list[i])
        ans %= mod
    elif a_confirm_list[i] is not None and a_confirm_list[i] > t_list[i]:
            ans = 0
    elif t_confirm_list[i] is not None and t_confirm_list[i] > a_list[i]:
            ans = 0

print(ans)    
