def main():
    n=int(input())
    v=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=[v[i] - c[i] for i in range(n)]
    print(sum((x for x in d if x > 0)))
    
if __name__ == "__main__":
    main()