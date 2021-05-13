def divs(n):
    res = []
    i = 1
    while i**2 <= n:
        if n%i == 0: 
            res.append(i)
            if i**2 != n:
                res.append(n//i)
        i+=1 
    return res


def main():
    n = int(input())
    al_0 = list(map(int, input().split()))
    if sum(al_0) == 0:
        print(0)
        return

    al = [0] + al_0
    divs_cnts = [0]*(n+1)
    ans = []
    for i in range(n,0,-1):
        if divs_cnts[i]%2 != al[i]%2:
            ans.append(i)
            div_l = divs(i)
            for d in div_l:
                divs_cnts[d] += 1

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()