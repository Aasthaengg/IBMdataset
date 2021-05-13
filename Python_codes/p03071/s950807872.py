def main():
    a,b=map(int,input().split())
    if a == b:
        print(a+b)
    else:
        m = max(a,b)
        print(m*2-1)
    
if __name__ == "__main__":
    main()