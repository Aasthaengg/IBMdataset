def main():
    n = int(input())
    a = list(map(lambda x: int(x)*2, input().split()))
    # x1を求める（最終的に2x1 = ~~となる）
    ans = 0
    for i in a:
        ans = i - ans
    ans = round(ans / 2)
    # x1がもとまったら、順に解いていく
    res = list()
    res.append(ans)
    for i in range(n-1):
        res.append(a[i] - res[i])
    for i in res: 
        print(i, end=' ')

if __name__ == '__main__':
    main()