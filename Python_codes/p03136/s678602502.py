def main():
    n=int(input())
    l=sorted(map(int,input().split()))
    print("Yes" if l[-1] < sum(l[:-1]) else "No")
    
if __name__ == "__main__":
    main()