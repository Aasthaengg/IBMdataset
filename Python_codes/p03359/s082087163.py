def ABC_96_A():
    a,b = map(int, input().split())
    
    if a <= b:
        print(a)
    else:
        print(a-1)

if __name__ == '__main__':

    ABC_96_A()