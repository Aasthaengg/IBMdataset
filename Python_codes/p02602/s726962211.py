def main():
    n,k=map(int,input().split())
    li=map(int,input().split())
    x=list(li)
    a=x[0:k]
    for i in range(k,n):
        if(a[0]<x[i]):
            print('Yes')
        else:
            print('No')
        del a[0]
        a.append(x[i])
    
main()
