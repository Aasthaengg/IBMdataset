
def main():
    n, k = map(int, input().split(" "))
    x = n % k 
    print(min(x,abs(x-k)))

if __name__ == "__main__":
    main()