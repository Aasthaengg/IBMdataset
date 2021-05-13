def main():
    n,m=map(int,input().split())
    k = [list(map(int,input().split())) for _ in range(n)]
    f = [0] * m
    for i in k:
        for j in i[1:]:
            f[j-1] += 1
    print(f.count(n))
    
if __name__ == "__main__":
    main()