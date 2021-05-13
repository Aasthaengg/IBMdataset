if __name__ == '__main__':
    H = int(input())
    cnt = 0
    while H!=1:
        H //= 2
        cnt += 1
    
    ans = 0
    for c in range(cnt+1):
        ans += pow(2, c)
    
    print(ans)