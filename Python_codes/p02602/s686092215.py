def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    p  = 0
 
    for i in range(K-1,N):
        #lst= A[i-K+1:i+1]
        #p = sum(lst)
        #p = mul(lst)
        #p = functools.reduce(operator.mul,lst)
        if i != K-1:
            if A[i] <= A[i-K]:
                print('No')
            else:
                print('Yes')
        
    
if __name__ == "__main__":
    main()
