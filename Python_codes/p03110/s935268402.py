def main():
    N = int(input())
    x = []
    ans = 0
    for i in range(N):
        x.append(list(map(str, input().split(' '))))
    for i in range(N):
        if x[i][1] == 'BTC':
            ans = ans + (float(x[i][0])*380000)
        else:
            ans += float(x[i][0])
    print(ans)
main()

