from sys import stdin

n,m,x = [int(x) for x in stdin.readline().split()]
a_lst = [int(x) for x in stdin.readline().split()]

cost_left = sum([1 for i in range(0, x) if i in a_lst])
cost_right = sum([1 for i in range(x+1, n+1) if i in a_lst])

print(min(cost_left, cost_right))