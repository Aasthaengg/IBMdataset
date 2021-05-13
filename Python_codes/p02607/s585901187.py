def main():
    n = int(input())
    
    a = list(map(int,input().split()))
    a = [0] + a
    
    count = 0
    for i in range(1,n+1):
        if i%2==1 and a[i]%2==1:
            count+=1
    print(count)
    
if __name__=='__main__':
    main()
