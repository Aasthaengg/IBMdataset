def main():
    n = int(input())
    
    z = []
    w = []

    for _ in range(n):
        x,y = tuple(map(int,input().split()))
        z.append(x+y)
        w.append(x-y)

    print(max(max(z)-min(z),max(w)-min(w)))

if __name__ == "__main__":
    main()