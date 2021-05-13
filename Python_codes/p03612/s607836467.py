def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    cnt = 0
    i = 0
    for i in range(N):
        if P[i] == i+1:
            if i+1 >= N:
                P[i],P[i-1] = P[i-1],P[i]
            else:
                P[i],P[i+1] = P[i+1],P[i]
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()