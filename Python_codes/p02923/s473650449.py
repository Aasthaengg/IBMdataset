def main():
    n = int(input())
    h = list(map(int, input().split()))
    maxv = 0
    cnt = 0
    for i in range(n-1):
        if h[i+1] <= h[i]:
            cnt += 1
        else:
            maxv = max(maxv, cnt)
            cnt = 0    
    maxv = max(maxv, cnt)
    print(maxv)
     
if __name__ == '__main__':
    main()