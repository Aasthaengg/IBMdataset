import math



n = int(input())
num_list = list(map(int,input().split()))

gcd = num_list[0]
mult = 1

for i in range(n):
    gcd = math.gcd(gcd,num_list[i])
    mult = mult*num_list[i]

mod_num = gcd*mult-1

c = 0

for i in range(n):
    c += mod_num % num_list[i]

print(c)