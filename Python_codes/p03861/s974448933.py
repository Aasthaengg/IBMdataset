a,b,x=[int(i) for i in input().split()]

def get_mod_num(limit,x):
    if limit==-1:
        return 0
    return limit//x+1

print(get_mod_num(b,x)-get_mod_num(a-1,x))