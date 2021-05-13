def main():
    a,b = map(int, input().split())
    
    print(a if b >= a else a-1)

if __name__ == "__main__":
    main()
