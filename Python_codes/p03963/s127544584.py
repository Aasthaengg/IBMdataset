def main():
    n,k=map(int,input().split())
    x=k-1
    for i in range(1,n):
        k*=x
    print(k)
    
main()
