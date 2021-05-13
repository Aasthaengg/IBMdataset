def cooking_takoyaki(target_num, cook_per, need_time):
    div, mod =divmod(target_num, cook_per)
    if mod == 0:
        return div * need_time
    return div * need_time + need_time

if __name__=='__main__':
    a, b, c = map(int, input().split())
    print(cooking_takoyaki(a, b, c))