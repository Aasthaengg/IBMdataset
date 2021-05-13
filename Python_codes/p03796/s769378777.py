def main():
    N = int(input())
    sum=1
    for i in range(1,N+1):
        sum*=i
        sum=sum%1000000007 
    print(sum)


    
if __name__ == '__main__':
    main()
