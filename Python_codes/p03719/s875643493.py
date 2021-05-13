#Between Two Integers
def ABC_61_A():
    A,B,C = map(int, input().split())
    
    if C>=A and C<=B:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':

    ABC_61_A()