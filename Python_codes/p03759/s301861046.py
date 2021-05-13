# ι⊥l
def ABC_58_A():
    A,B,C = map(int, input().split())
    
    if B == (A+C)/2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':

    ABC_58_A()