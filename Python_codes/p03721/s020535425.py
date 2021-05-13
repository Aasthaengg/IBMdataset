def main():
    n,k=map(int,input().split())
    arr = []
    for _ in range(n):
        a,b=map(int,input().split())
        arr.append((a, b))
    arr.sort()
    for x, c in arr:
        if k <= c:
            print(x)
            break
        else:
            k -= c
    
if __name__ == "__main__":
    main()