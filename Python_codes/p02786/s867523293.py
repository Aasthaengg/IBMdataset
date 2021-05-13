h = int(input())

def calc_need_atack_num(h):
    if h == 1:
        return 1
    return calc_need_atack_num(h//2) * 2 + 1

print(calc_need_atack_num(h))