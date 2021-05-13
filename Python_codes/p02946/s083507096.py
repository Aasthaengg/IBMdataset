def main():
    k, x = map(int, input().split())
    a = list(range(x-k+1, x+k))
    print(*a)
    
if __name__ == '__main__':
    main()