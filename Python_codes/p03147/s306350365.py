def main():
    n = int(input())
    inlis = list(map(int, input().split()))

    tmp = 0
    ans = 0
    goukei = sum(inlis)
    while goukei > 0:
        for i in range(n):
            if inlis[i] > 0:
                #print(inlis)
                inlis[i] -= 1
                tmp += 1
                ans += 1
            else:
                if tmp > 0:
                    ans -= tmp - 1
                    tmp = 0
        if tmp > 0:
            ans -= tmp - 1
            tmp = 0
        goukei = sum(inlis)
        #print(ans, inlis, tmp)
        

    print(ans)

            



if __name__ == "__main__":
    main()