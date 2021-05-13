import math
n,m = map(int,input().split())
s = input()
t = input()
lcm = n*m//math.gcd(n,m)
ans = []
s_ind = lcm//n
t_ind = lcm//m
check_ind = s_ind*t_ind//math.gcd(s_ind,t_ind)
for i in range(0,lcm,check_ind):
    if s[i//s_ind] != t[i//t_ind]:
        print(-1)
        exit()
print(lcm)