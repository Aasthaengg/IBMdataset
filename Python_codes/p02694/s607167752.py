def main(money, X):
    ans = 0
    while money < X:
        money += money//100
        ans += 1
    return ans

if __name__ == '__main__':
    money = 100
    X = int(input())
    ans = main(money, X)
    print(ans)

