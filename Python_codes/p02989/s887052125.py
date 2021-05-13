from sys import stdin

n = int(stdin.readline().strip())
d_lst = sorted([int(x) for x in stdin.readline().strip().split()])

bef = d_lst[len(d_lst)//2-1]
aft = d_lst[len(d_lst)//2]

print(aft - bef)