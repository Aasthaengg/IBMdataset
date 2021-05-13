S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
LS=lambda:list(map(str,input().split()))

def main():
    a,b,c=L()
    c=c-(a-b) if c>=a-b else 0
    print(c)

if __name__=='__main__':
    main()