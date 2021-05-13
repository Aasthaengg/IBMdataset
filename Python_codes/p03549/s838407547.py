def main():
    n,m=map(int, input().split())
    t1 = 100 * (n-m)
    t2 = 1900 * m
    kaisu = 1/((1/2)**m)
    print(int((t1+t2)*kaisu))
    
if __name__ == "__main__":
    main()