if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    cnt = 1
    
    if 1 not in a:
        print(-1)
    else:
        for i in a:
            if i == cnt:
                cnt += 1
            else:
                ans += 1
        print(ans)