def main():
    n = int(input())
    A = list(map(int, input().split()))

    A_sorted = sorted(A)[::-1]
    teams = list([] for _ in range(n))
    idx = 0
    count = 0

    for score in A_sorted:
        teams[idx].append(score)
        
        count += 1

        if count == 2:
            if idx == n -1:
                idx = 0
            else:
                idx += 1
            
            count = 0
    
    res = 0

    for team in teams:
        res += team[1]
    
    print(res)

if __name__ == '__main__':
    main()