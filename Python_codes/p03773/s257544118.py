#Remaining Time
def ABC_57_A():
    A,B = map(int, input().split())
    
    if A+B < 24:
        print(A+B)
    else:
        print(A+B-24)

if __name__ == '__main__':

    ABC_57_A()