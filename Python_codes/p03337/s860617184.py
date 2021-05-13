def ABC_98_A():
    A,B = map(int, input().split())
    
    print(max(A+B,A-B,A*B))

if __name__ == '__main__':

    ABC_98_A()