_ = int(input())
v_list = [int(x) for x in input().split()]
c_list = [int(x) for x in input().split()]
p_list = [v - c for v, c in zip(v_list, c_list) if v - c > 0]
print(sum(p_list))