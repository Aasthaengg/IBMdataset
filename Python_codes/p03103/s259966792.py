def main():
    n,m=map(int,input().split())
    s=[tuple(map(int,input().split())) for _ in range(n)]
    s.sort(key=lambda x: x[0])
    bought = 0
    cost = 0
    for yen, ko in s:
        cost += ko*yen
        bought += ko
        #print(cost, bought, m)
        if bought >= m:
            cost -= (bought-m)*yen
            break
    print(cost)
    
if __name__ == "__main__":
    main()