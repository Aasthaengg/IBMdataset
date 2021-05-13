# https://atcoder.jp/contests/abc081/tasks/abc081_b
N = int(input())
int_list = list(map(int, input().split()))

def check_even(int_list):
    for i in int_list:
        if i % 2 == 1:
            return False
    else:
        return True

def half_list(int_list):
    return [i / 2 for i in int_list]
    
for i in range(50):
    if check_even(int_list):
        int_list = half_list(int_list)
    else:
        print(i)
        break