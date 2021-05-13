import math
n = int(input())
p_ls = list(map(int, input().split()))
q_ls = list(map(int, input().split()))

def dict_num(ls):
    m = len(ls)
    ans = 0
    already = []
    for i in range(m):
        top = ls[i]
        for j in range(1,top):
            if j not in already:
                ans += math.factorial(m-i-1)
        already.append(top)
    return ans+1
print(abs(dict_num(q_ls)-dict_num(p_ls)))