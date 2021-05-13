def get_num():
    n = int(input())
    w = int(input())
    return n,w

def check_range(n,w):
    return n in range(1,101) and w in range(n**2+1)

def black_tiles(n,w):
    if (check_range(n,w)):
        return n**2 - w
    else:
        raise Exception('Value out of range')

if (__name__=='__main__'):
    print(black_tiles(*get_num()))