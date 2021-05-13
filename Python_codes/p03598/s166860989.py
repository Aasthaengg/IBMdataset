from sys import stdin

n = int(stdin.readline().strip())
k = int(stdin.readline().strip())
x_lst = [int(x) for x in stdin.readline().strip().split()]
sum_move = 0

# 絶対値の小さい方で和を取ればいいだけ
for x in x_lst:
  sum_move += min(abs(k-x), abs(x)) * 2
  
print(sum_move)