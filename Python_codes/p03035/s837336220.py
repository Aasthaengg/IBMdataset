def resolve():
    #n=int(input())
    #a,b=map(int,input().split())
    #x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    a,b=map(int,input().split())
    if a>=13:
        print(b)
    elif a>=6:
        print(b//2)
    else:
        print(0)
    

if __name__ == '__main__':
    resolve()
