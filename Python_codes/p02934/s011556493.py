def main():
    n = int(input())
    a = map(int, input().split())
    x = []
    for i in a:
        x.append(1/i)
    print(1/sum(x))
    
if __name__ == "__main__":
    main()