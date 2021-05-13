def main():
    k,x=map(int,input().split())
    limit = 1000001
    left = max(x-k, -limit) + 1
    right = min(x+k, limit)
    print(*range(left, right))

if __name__ == "__main__":
    main()