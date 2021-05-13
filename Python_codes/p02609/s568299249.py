def resolve():
    #n=int(input())
    #a,b=map(int,input().split())
    #x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]

    def popcount(n):
        c=format(n,'b').count('1')
        if c!=0:
            return n%c
        else:
            return 0
    def f(n):
        count=0
        while n>0:
            n=popcount(n)
            count+=1
        return count
        
    n=int(input())    
    x=input()
    cnt=x.count('1')
    x10=int(x,2)
    ans=[]
    a=x10%(cnt+1)
    if cnt==1:
        b=0
    else:
        b=x10%(cnt-1)
    for i in range(n):
        if x[i]=='1' and cnt==1:
            print(0)
            continue
        elif x[i]=='1':
            cal=(b-pow(2,n-1-i,cnt-1))%(cnt-1)
        else:
            cal=(a+pow(2,n-1-i,cnt+1))%(cnt+1)
        print(f(cal)+1)

if __name__ == '__main__':
    resolve()