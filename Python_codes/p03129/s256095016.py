def main():
    N,K = map(int,input().split())
    if N%2==0:
        pass
    else:
        N += 1
    
    if K<=N//2:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    main()