def ABC_97_A():
    a,b,c,d = map(int, input().split())
    
    if (abs(b-a) <= d and abs(c-b) <= d) or abs(c-a) <= d:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':

    ABC_97_A()