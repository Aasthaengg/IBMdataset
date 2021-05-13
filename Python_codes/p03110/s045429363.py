def main():
    N = int(input())
    money = [input().split() for i in range(N)]
    total = 0
    for i in range(N):
        [x, u] = money[i]
        if u == "JPY":
            total += float(x)
        else:
            total += float(x)*380000.0
    print(total)
main()