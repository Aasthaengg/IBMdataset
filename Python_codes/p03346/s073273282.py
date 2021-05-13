def main():
    n = int(input())
    p = []
    for _ in range(n):
        p.append(int(input()))
    q = [0 for i in range(n)]
    for i in range(n):
        q[p[i]-1] = i
    m,cnt = 1,1
    for i in range(1,n):
        if q[i]>q[i-1]:
            cnt += 1
            if cnt > m:
                m = cnt
        else:
            cnt = 1
    print(n-m)

if __name__ == "__main__":
    main()