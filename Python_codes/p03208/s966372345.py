def main():
    n,k=map(int,input().split())
    h=sorted(int(input()) for _ in range(n))
    hs = []
    for i in range(n-k+1):
        hs.append(h[i+k-1] - h[i])
    print(min(hs))
    
    
if __name__ == "__main__":
    main()