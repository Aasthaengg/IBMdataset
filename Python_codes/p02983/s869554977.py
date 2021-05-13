def main():
    L,R = [int(x) for x in input().split()]
    ans = 2019
    for i in range(L,min(R,L+2018)+1):
        for j in range(i+1,min(R,L+2018)+1):
            tmp = (i*j) % 2019
            if tmp < ans:
                ans = tmp
    print(ans)

if __name__ == '__main__':
    main()