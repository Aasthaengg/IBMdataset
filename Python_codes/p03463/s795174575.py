
def main():
    N,A,B  = map(int, input().split()) 
    while True:
        if(A+1==B):
            print('Borys')
            return
        A = A+1
        if(B-1==A):
            print('Alice')
            return
        B = B-1


if __name__ == '__main__':
    main()
