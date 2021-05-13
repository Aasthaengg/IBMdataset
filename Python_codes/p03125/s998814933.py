# coding: utf-8
# Your code here!

N = input().split()
N_map = map(int,N)

N_list = [x for x in N_map]
a = N_list[0]
b = N_list[1]

if b % a == 0:
    print(b+a)

else:
    print(b-a)