def main():
    N,T=map(int,input().split())
    t=list(map(int,input().split()))
    s = 0
    c = 0
    for t1 in t:
        c = max(c, t1)
        if c > t1:
            s += t1 - c + T
            c += t1 - c + T
        else:
            s += T
            c += T
    print(s)
    
if __name__ == "__main__":
    main()