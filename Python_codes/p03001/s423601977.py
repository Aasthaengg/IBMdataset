S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
LS=lambda:list(map(str,input().split()))

def main():
    w,h,x,y=L()
    print(w*h/2,end=" ")
    print(1 if w/2==x and h/2==y else 0)
    

if __name__=='__main__':
    main()