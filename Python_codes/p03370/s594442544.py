def main():
    n,x=map(int,input().split())
    m=[int(input()) for _ in range(n)]
    sum_m=sum(m)
    min_m=min(m)
    ans=len(m)
    x-=sum_m
    ans+=x//min_m
    print(ans)

if __name__ == "__main__":
    main()