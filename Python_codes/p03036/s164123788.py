def main():
    r, d, x = map(int, input().split())
    
    for i in range(1, 11):
        x = r*x - d
        print(x)

if __name__ == "__main__":
    main()
