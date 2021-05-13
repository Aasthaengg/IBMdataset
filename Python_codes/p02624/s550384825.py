def main():
    n = int(input())
    s = 0
    for i in range(1,n+1):
        s += i * (1+n//i) * (n//i) //2
    print(s)
    
if __name__ == "__main__":
    main()
