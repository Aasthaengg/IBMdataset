def main():
    n,x,t = map(int,input().split())
    base = int(n/x)
    if n%x != 0:
        base += 1
    
    print(base*t)


if __name__ == "__main__":
    main() 