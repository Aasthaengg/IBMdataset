def ABC_87_A():
    X = int(input())
    A = int(input())
    B = int(input())
    
    B_buy = int((X-A)/B)
    print(X-A-B*B_buy)



if __name__ == '__main__':

    ABC_87_A()