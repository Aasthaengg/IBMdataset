S = input()
total_p = sum([ 1 for i in S if i == '+' ])
total_m = sum([-1 for j in S if j == '-'])
print(total_p + total_m)