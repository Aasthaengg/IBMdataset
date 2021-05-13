S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
LS=lambda:list(map(str,input().split()))

def main():
    p,q,r=L()
    print(min(p+q,q+r,r+p))

if __name__=='__main__':
    main()