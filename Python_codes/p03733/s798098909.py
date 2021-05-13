from sys import stdin

n,t = [int(x) for x in stdin.readline().strip().split()]
t_lst = [int(x) for x in stdin.readline().strip().split()]
diff_lst = [min(t, t_lst[i+1]-t_lst[i]) for i in range(len(t_lst)-1)]
print(sum(diff_lst) + t)