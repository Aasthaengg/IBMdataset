mod = 1e9+7
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    A, B = [x for x in raw_input().split()]
    
    A_cnt, B_cnt = [int(x) for x in raw_input().split()]
    
    throw_away = raw_input()
    
    if throw_away == A:
        A_cnt -= 1
    else:
        B_cnt -= 1
    
    print(str(A_cnt) + " " + str(B_cnt))
    

main()