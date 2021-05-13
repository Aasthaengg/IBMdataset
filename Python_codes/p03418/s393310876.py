def main():
    n,k = map(int,input().split())
    s = 0
    if k==0:
        s = n*n
    else:
        for k_ in range(k,n):
            for q in range((n-k_)//(k_+1)+1):
                if q==0:
                    s += n-k_
                else:
                    s += (n-k_)//q-k_
    print(s)
            
if __name__ == "__main__":
    main()