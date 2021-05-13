S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
def main():
    H,W=L()
    h,w=L()
    print(H*W-h*W-(w*(H-h)))
    

if __name__ == '__main__':
    main()