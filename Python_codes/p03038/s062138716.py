def main():
    n,m=map(int,input().split())
    a=sorted(map(int,input().split()))
    bc=[list(map(int,input().split())) for _ in range(m)]
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b,c in bc:
        for _ in range(b):
            if i < len(a) and a[i] < c:
                a[i] = c
                i += 1
            else:
                print(sum(a))
                return
    print(sum(a))
    
if __name__ == "__main__":
    main()