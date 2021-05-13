def main():
    a=sorted(map(int,input().split()))
    print(abs(a[1]-a[0]) + abs(a[2]-a[1]))
    
if __name__ == "__main__":
    main()