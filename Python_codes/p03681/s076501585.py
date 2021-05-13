def main():
    m,n = map(int,input().split())
    if abs(m-n) > 1:
        print(0)
        return
        
    c = 1
    w = 10**9+7
    for i in range(2, min(m, n)+1):
        c = (c * i) % w
    
    if m == n:
        nc = (c * 2) % w
    else:
        nc = (c * max(m, n)) % w
    
    print(c*nc%w)
    
if __name__ == "__main__":
    main()