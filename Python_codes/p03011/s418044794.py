def main():
    x = list(map(int, input().split()))
    print(sum(x) - max(x))
    
if __name__ == "__main__":
    main()