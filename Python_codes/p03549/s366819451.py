def main():
    n, m = map(int, input().split())
    t = 1900 * m + 100 * (n-m)
    a = (1/2) ** m
    r = 1 - a

    print(int(a*t / ((1-r)**2)))
 
    
    
if __name__ == "__main__":
    main()