def resolve():
    #n=int(input())
    #a,b=map(int,input().split())
    #x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    r,d,x=map(int,input().split())
    for i in range(10):
        x=r*x-d
        print(x)
    
    
if __name__ == '__main__':
    resolve()